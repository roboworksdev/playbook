#!/usr/bin/env python3
"""Robby Chronicles — Teach the Teacher curriculum companion for RoboSim5."""

import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error

from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import (
    QBrush, QColor, QFont, QPalette, QPainter, QPainterPath, QPen, QPixmap, QIcon,
)
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMessageBox, QPushButton, QScrollArea, QSizePolicy, QSplitter,
    QTextEdit, QVBoxLayout, QWidget,
)

from curriculum import CHAPTERS, script_path, world_path

# ─── Embedded RoboSim ────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "RoboSim"))
from RobotSim5 import MainWindow as RoboSimWindow

# ─── Paths ────────────────────────────────────────────────────────────────────

_APP_DIR       = os.path.dirname(os.path.abspath(__file__))
_ROBOSIM       = os.path.join(_APP_DIR, "RoboSim")
_GIT_CREDS_FILE  = os.path.join(_APP_DIR, ".git_credentials.json")
_EDU_NOTES_FILE  = os.path.join(_APP_DIR, ".educator_notes.json")

# ─── Colours ──────────────────────────────────────────────────────────────────

C_BG      = "#1C1C1E"
C_SIDEBAR = "#2C2C2E"
C_SURFACE = "#2C2C2E"
C_CARD    = "#2C2C2E"
C_BORDER  = "#3A3A3C"
C_TEXT    = "#F2F2F7"
C_SUB     = "#8E8E93"
C_ACCENT  = "#0A84FF"
C_GREEN   = "#30D158"
C_ORANGE  = "#FF9F0A"
C_PURPLE  = "#BF5AF2"
C_RED     = "#FF453A"

# ─── Shared styles ────────────────────────────────────────────────────────────

# ─── Educator-notes persistence ───────────────────────────────────────────────

def _load_edu_notes() -> dict:
    try:
        with open(_EDU_NOTES_FILE, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def _save_edu_notes(notes: dict):
    with open(_EDU_NOTES_FILE, "w", encoding="utf-8") as fh:
        json.dump(notes, fh, indent=2)


# ─── Shared button styles ─────────────────────────────────────────────────────

_BTN_BLUE = f"""
    QPushButton {{
        background: {C_ACCENT}; color: white; border: none;
        border-radius: 8px; font-size: 12px; padding: 5px 14px;
    }}
    QPushButton:hover   {{ background: #0070E0; }}
    QPushButton:pressed {{ background: #005EC5; }}
"""
_BTN_GREY = f"""
    QPushButton {{
        background: #3A3A3C; color: {C_TEXT}; border: none;
        border-radius: 8px; font-size: 12px; padding: 5px 14px;
    }}
    QPushButton:hover   {{ background: #48484A; }}
    QPushButton:pressed {{ background: #555; }}
"""
_BTN_GHOST = f"""
    QPushButton {{
        background: transparent; color: {C_ACCENT}; border: none;
        font-size: 12px; padding: 4px 10px; border-radius: 6px;
    }}
    QPushButton:hover {{ background: #3A3A3C; }}
"""


# ─── CollapsibleSection ───────────────────────────────────────────────────────

class CollapsibleSection(QWidget):
    """A labelled section with a ▶/▼ toggle that shows/hides its content."""

    def __init__(self, title: str, content_widget: QWidget,
                 accent: str = C_ACCENT, collapsed: bool = True,
                 font_delta: int = 0, parent=None):
        super().__init__(parent)
        self._collapsed = collapsed

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header row
        hdr = QWidget()
        hdr.setStyleSheet(f"background: #252527; border-radius: 8px;")
        hdr.setCursor(Qt.CursorShape.PointingHandCursor)
        hl = QHBoxLayout(hdr)
        hl.setContentsMargins(14, 10, 14, 10)

        self._arrow = QLabel("▶" if collapsed else "▼")
        self._arrow.setStyleSheet(f"color: {accent}; font-size: 17px;")
        self._arrow.setFixedWidth(14)

        lbl = QLabel(title)
        lbl.setFont(QFont("Helvetica Neue", 20 + font_delta, QFont.Weight.Bold))
        lbl.setStyleSheet(f"color: {C_TEXT};")

        hl.addWidget(self._arrow)
        hl.addWidget(lbl)
        hl.addStretch()
        layout.addWidget(hdr)

        # Content
        self._content = content_widget
        self._content.setVisible(not collapsed)
        layout.addWidget(self._content)

        hdr.mousePressEvent = lambda _: self._toggle()

    def _toggle(self):
        self._collapsed = not self._collapsed
        self._arrow.setText("▶" if self._collapsed else "▼")
        self._content.setVisible(not self._collapsed)

    def expand(self):
        if self._collapsed:
            self._toggle()

    def collapse(self):
        if not self._collapsed:
            self._toggle()


# ─── MissionRow ───────────────────────────────────────────────────────────────

_BTN_WHITE = f"""
    QPushButton {{
        background: black; color: white; border: 1px solid #444;
        border-radius: 8px; font-size: 12px; padding: 5px 14px; font-weight: 600;
    }}
    QPushButton:hover {{ background: #1a1a1a; }}
    QPushButton:disabled {{ background: #2a2a2a; color: #555; border-color: #333; }}
"""

class MissionRow(QWidget):
    """One mission: checkbox, id, title, description, action buttons."""

    def __init__(self, mission: dict, on_open_script, font_delta: int = 0,
                 on_open_editor=None, on_run=None, on_stop=None, on_reset=None, parent=None):
        super().__init__(parent)
        self._script = mission.get("script", "")
        self._on_open = on_open_script

        self.setStyleSheet(f"""
            QWidget {{
                background: #252527;
                border-radius: 8px;
            }}
        """)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(14, 12, 14, 12)
        outer.setSpacing(4)

        # Top row: id + title + Open button
        top = QHBoxLayout()
        top.setSpacing(10)

        self._check = QLabel("●")
        self._check.setFixedWidth(18)
        self._check.setFont(QFont("Helvetica Neue", 14 + font_delta))
        self._check.setStyleSheet(f"color: {C_SUB};")
        top.addWidget(self._check)

        id_lbl = QLabel(mission['id'])
        id_lbl.setFont(QFont("Helvetica Neue", 17 + font_delta, QFont.Weight.Bold))
        id_lbl.setStyleSheet(f"color: {C_ACCENT};")
        top.addWidget(id_lbl)

        title_lbl = QLabel(mission["title"])
        title_lbl.setFont(QFont("Helvetica Neue", 20 + font_delta, QFont.Weight.Medium))
        title_lbl.setStyleSheet(f"color: {C_TEXT};")
        top.addWidget(title_lbl, stretch=1)

        if self._script:
            open_btn = QPushButton("Starter Code ▶")
            open_btn.setStyleSheet(_BTN_GHOST)
            open_btn.setFixedHeight(28)
            open_btn.clicked.connect(self._open_script)
            top.addWidget(open_btn)

        outer.addLayout(top)

        # Description
        desc = QLabel(mission["description"])
        desc.setFont(QFont("Helvetica Neue", 18 + font_delta))
        desc.setStyleSheet(f"color: {C_TEXT}; padding-left: 28px;")
        desc.setWordWrap(True)
        outer.addWidget(desc)

        # Action buttons row
        btn_row = QHBoxLayout()
        btn_row.setContentsMargins(28, 6, 0, 0)
        btn_row.setSpacing(8)

        editor_btn = QPushButton("Code Editor")
        editor_btn.setStyleSheet(_BTN_WHITE)
        editor_btn.setFixedHeight(30)
        if on_open_editor:
            editor_btn.clicked.connect(on_open_editor)
        btn_row.addWidget(editor_btn)

        run_btn = QPushButton("Run")
        run_btn.setStyleSheet(_BTN_WHITE)
        run_btn.setFixedHeight(30)
        if on_run:
            run_btn.clicked.connect(on_run)
        btn_row.addWidget(run_btn)

        stop_btn = QPushButton("Stop")
        stop_btn.setStyleSheet(_BTN_WHITE)
        stop_btn.setFixedHeight(30)
        if on_stop:
            stop_btn.clicked.connect(on_stop)
        btn_row.addWidget(stop_btn)

        reset_btn = QPushButton("Reset")
        reset_btn.setStyleSheet(_BTN_WHITE)
        reset_btn.setFixedHeight(30)
        if on_reset:
            reset_btn.clicked.connect(on_reset)
        btn_row.addWidget(reset_btn)

        btn_row.addStretch()
        outer.addLayout(btn_row)

    def _open_script(self):
        if self._on_open:
            self._on_open(self._script)

    def mark_complete(self, done: bool):
        color = C_GREEN if done else C_SUB
        self._check.setStyleSheet(f"color: {color};")


# ─── ScriptPanel ──────────────────────────────────────────────────────────────

class ScriptPanel(QWidget):
    """Inline script viewer with Copy and Open in Editor buttons."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setVisible(False)
        self.setStyleSheet(f"background: #1A1A1C; border-radius: 10px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header bar
        hdr = QWidget()
        hdr.setStyleSheet(f"background: #252527; border-radius: 10px 10px 0 0;")
        hl = QHBoxLayout(hdr)
        hl.setContentsMargins(14, 8, 10, 8)

        self._title_lbl = QLabel("")
        self._title_lbl.setFont(QFont("Helvetica Neue", 12, QFont.Weight.Bold))
        self._title_lbl.setStyleSheet(f"color: {C_TEXT};")
        hl.addWidget(self._title_lbl, stretch=1)

        font_sm_btn = QPushButton("a")
        font_sm_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 3px 8px; font-size: 11px; }")
        font_sm_btn.setFixedHeight(26)
        font_sm_btn.setToolTip("Decrease font size")
        font_sm_btn.clicked.connect(lambda: self._adjust_font(-1))
        hl.addWidget(font_sm_btn)

        font_lg_btn = QPushButton("A")
        font_lg_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 3px 8px; font-size: 15px; font-weight: bold; }")
        font_lg_btn.setFixedHeight(26)
        font_lg_btn.setToolTip("Increase font size")
        font_lg_btn.clicked.connect(lambda: self._adjust_font(+1))
        hl.addWidget(font_lg_btn)

        copy_btn = QPushButton("Copy")
        copy_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 3px 12px; font-size: 11px; }")
        copy_btn.setFixedHeight(26)
        copy_btn.clicked.connect(self._copy)
        hl.addWidget(copy_btn)

        close_btn = QPushButton("✕")
        close_btn.setStyleSheet(_BTN_GHOST + "QPushButton { color: #8E8E93; padding: 3px 8px; }")
        close_btn.setFixedSize(28, 26)
        close_btn.clicked.connect(lambda: self.setVisible(False))
        hl.addWidget(close_btn)

        layout.addWidget(hdr)

        # Code viewer
        self._font_size = 12
        self._viewer = QTextEdit()
        self._viewer.setReadOnly(True)
        self._viewer.setFont(QFont("Menlo", self._font_size))
        self._viewer.setStyleSheet(f"""
            QTextEdit {{
                background: #1A1A1C; color: #E5E5EA;
                border: none; padding: 12px;
            }}
        """)
        self._viewer.setMinimumHeight(260)
        layout.addWidget(self._viewer)

        self._current_path = ""

    def load_text(self, title: str, code: str):
        """Display inline code text (no file needed)."""
        self._current_path = ""
        self._title_lbl.setText(title)
        self._viewer.setPlainText(code)
        self.setVisible(True)
        self._viewer.verticalScrollBar().setValue(0)

    def _adjust_font(self, delta: int):
        self._font_size = max(8, min(24, self._font_size + delta))
        self._viewer.setFont(QFont("Menlo", self._font_size))

    def _copy(self):
        QApplication.clipboard().setText(self._viewer.toPlainText())

    def _open_external(self):
        if self._current_path and os.path.isfile(self._current_path):
            subprocess.run(["open", self._current_path])


# ─── ConceptChip ─────────────────────────────────────────────────────────────

def _concept_chip(text: str) -> QLabel:
    lbl = QLabel(text)
    lbl.setFont(QFont("Helvetica Neue", 17))
    lbl.setStyleSheet(f"""
        color: {C_PURPLE};
        background: #2D1F3D;
        border: 1px solid #4A2E6B;
        border-radius: 10px;
        padding: 2px 10px;
    """)
    return lbl


# ─── ChapterView ─────────────────────────────────────────────────────────────

class ChapterView(QWidget):
    """Full content panel for one chapter."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._teacher_mode = False
        self._font_delta = 0
        self._current_chapter = None
        self._robosim_win = None

    def set_robosim(self, win):
        self._robosim_win = win

        # Outer scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet(f"background: {C_BG};")
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._inner = QWidget()
        self._inner.setStyleSheet(f"background: {C_BG};")
        self._vl = QVBoxLayout(self._inner)
        self._vl.setContentsMargins(32, 24, 32, 32)
        self._vl.setSpacing(20)
        scroll.setWidget(self._inner)

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.addWidget(scroll)

    def adjust_font(self, delta: int):
        self._font_delta = max(-4, min(8, self._font_delta + delta))
        if self._current_chapter:
            self.load(self._current_chapter, self._teacher_mode)

    def load(self, chapter: dict, teacher_mode: bool):
        self._current_chapter = chapter
        self._teacher_mode = teacher_mode
        d = self._font_delta
        # Clear
        while self._vl.count():
            item = self._vl.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        available = chapter["status"] == "available"

        # ── Chapter header ────────────────────────────────────────────────────
        num_lbl = QLabel("Introduction" if chapter['number'] == 0 else f"Chapter {chapter['number']}")
        num_lbl.setFont(QFont("Helvetica Neue", 18 + d, QFont.Weight.Bold))
        num_lbl.setStyleSheet(f"color: {C_ACCENT};")
        self._vl.addWidget(num_lbl)

        title_lbl = QLabel(chapter["title"])
        title_lbl.setFont(QFont("Helvetica Neue", 42 + d, QFont.Weight.Bold))
        title_lbl.setStyleSheet(f"color: {C_TEXT};")
        self._vl.addWidget(title_lbl)

        sub_lbl = QLabel(f'\u201c{chapter["subtitle"]}\u201d')
        sub_lbl.setFont(QFont("Helvetica Neue", 23 + d))
        sub_lbl.setStyleSheet(f"color: {C_SUB}; font-style: italic;")
        self._vl.addWidget(sub_lbl)

        # World file badge (hidden when no world file assigned)
        if chapter.get("world_file"):
            wf_row = QHBoxLayout()
            wf_lbl = QLabel("World file:")
            wf_lbl.setStyleSheet(f"color: {C_SUB}; font-size: 12px;")
            wf_val = QLabel(chapter["world_file"])
            wf_val.setStyleSheet(f"color: {C_ORANGE}; font-size: 12px; font-family: Menlo;")
            wf_row.addWidget(wf_lbl)
            wf_row.addWidget(wf_val)
            wf_row.addStretch()
            self._vl.addLayout(wf_row)

        # Concepts chips
        chips_row = QWidget()
        chips_l = QHBoxLayout(chips_row)
        chips_l.setContentsMargins(0, 0, 0, 0)
        chips_l.setSpacing(6)
        for c in chapter.get("concepts", []):
            chips_l.addWidget(_concept_chip(c))
        chips_l.addStretch()
        self._vl.addWidget(chips_row)

        self._vl.addWidget(_hline())

        if not available:
            coming = QLabel("This chapter is coming soon.")
            coming.setFont(QFont("Helvetica Neue", 23 + d))
            coming.setStyleSheet(f"color: {C_SUB};")
            coming.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._vl.addWidget(coming)
            self._vl.addStretch()
            return

        # ── Story ─────────────────────────────────────────────────────────────
        story_hdr = _section_label("STORY", d)
        self._vl.addWidget(story_hdr)

        story_body = QLabel(chapter["story"])
        story_body.setFont(QFont("Helvetica Neue", 21 + d))
        story_body.setStyleSheet(f"color: {C_TEXT}; line-height: 1.6;")
        story_body.setWordWrap(True)
        self._vl.addWidget(story_body)

        self._vl.addWidget(_hline())

        # ── Missions ──────────────────────────────────────────────────────────
        missions_hdr = _section_label("MISSIONS", d)
        self._vl.addWidget(missions_hdr)

        # Script panel (shared, shown below missions when Open Script clicked)
        self._script_panel = ScriptPanel()

        self._mission_rows = []
        rsw = self._robosim_win
        for m in chapter.get("missions", []):
            row = MissionRow(
                m,
                on_open_script=self._on_open_script,
                font_delta=d,
                on_open_editor=rsw.open_editor if rsw else None,
                on_run=rsw.run_active if rsw else None,
                on_stop=rsw.stop_active if rsw else None,
                on_reset=rsw.reset_world if rsw else None,
            )
            self._vl.addWidget(row)
            self._mission_rows.append(row)

        self._vl.addWidget(self._script_panel)
        self._vl.addWidget(_hline())

        # ── Learning Outcomes (Teacher Mode only) ─────────────────────────────
        self._lo_section = None
        if chapter.get("learning_outcomes"):
            self._lo_section = self._build_collapsible_text(
                "Learning Outcomes",
                chapter["learning_outcomes"],
                accent=C_ACCENT,
            )
            self._lo_section.setVisible(teacher_mode)
            self._vl.addWidget(self._lo_section)

        # ── Educator Notes (Teacher Mode only) ────────────────────────────────
        self._edu_section = self._build_edu_notes_section(chapter)
        self._edu_section.setVisible(teacher_mode)
        self._vl.addWidget(self._edu_section)

        self._vl.addStretch()

    def mark_mission_done(self, mission_num: int):
        """Mark mission at 1-based index as complete (green dot)."""
        idx = mission_num - 1
        if hasattr(self, "_mission_rows") and 0 <= idx < len(self._mission_rows):
            self._mission_rows[idx].mark_complete(True)

    def set_teacher_mode(self, enabled: bool):
        self._teacher_mode = enabled
        if hasattr(self, "_lo_section") and self._lo_section:
            self._lo_section.setVisible(enabled)
        if hasattr(self, "_edu_section"):
            self._edu_section.setVisible(enabled)

    def _on_open_script(self, code: str):
        self._script_panel.load_text("Starter Code", code)
        # Scroll to script panel
        QTimer.singleShot(50, self._scroll_to_script)

    def _scroll_to_script(self):
        sp = self._script_panel
        scroll = self.findChild(QScrollArea)
        if scroll and sp.isVisible():
            pos = sp.mapTo(self._inner, sp.rect().topLeft()).y()
            scroll.verticalScrollBar().setValue(pos - 20)

    def _build_collapsible_text(self, title: str, text: str, accent: str) -> CollapsibleSection:
        d = self._font_delta
        body = QLabel(text)
        body.setStyleSheet(
            f"color: {C_TEXT}; font-family: 'Helvetica Neue'; font-size: {20 + d}px;"
            f" padding: 14px; background: #1A1A1C; border-radius: 0 0 8px 8px;"
        )
        body.setWordWrap(True)
        body.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        return CollapsibleSection(title, body, accent=accent, collapsed=True, font_delta=d)

    def _build_edu_notes_section(self, chapter: dict) -> CollapsibleSection:
        d = self._font_delta
        chapter_key = str(chapter["number"])
        saved_notes = _load_edu_notes()
        has_saved = chapter_key in saved_notes
        initial_text = saved_notes[chapter_key] if has_saved else chapter["educator_notes"]

        body = QWidget()
        body.setStyleSheet("background: #1A1A1C; border-radius: 0 0 8px 8px;")
        bl = QVBoxLayout(body)
        bl.setContentsMargins(14, 12, 14, 12)
        bl.setSpacing(8)

        editor = QTextEdit()
        editor.setPlainText(initial_text)
        editor.setStyleSheet(f"""
            QTextEdit {{
                color: {C_TEXT}; background: #252527;
                border: 1px solid {C_BORDER}; border-radius: 6px;
                padding: 8px; font-family: 'Helvetica Neue'; font-size: {20 + d}px;
            }}
        """)
        editor.setReadOnly(has_saved)
        editor.setMinimumHeight(100)
        bl.addWidget(editor)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        save_btn = QPushButton("Edit" if has_saved else "Save")
        save_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 3px 14px; font-size: 11px; }")
        save_btn.setFixedHeight(28)
        btn_row.addWidget(save_btn)
        bl.addLayout(btn_row)

        def _on_btn():
            if editor.isReadOnly():
                editor.setReadOnly(False)
                save_btn.setText("Save")
                editor.setFocus()
            else:
                notes = _load_edu_notes()
                notes[chapter_key] = editor.toPlainText()
                _save_edu_notes(notes)
                editor.setReadOnly(True)
                save_btn.setText("Edit")

        save_btn.clicked.connect(_on_btn)
        return CollapsibleSection("Notes", body, accent=C_GREEN, collapsed=True, font_delta=d)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _hline() -> QFrame:
    line = QFrame()
    line.setFrameShape(QFrame.Shape.HLine)
    line.setStyleSheet(f"color: {C_BORDER};")
    return line


def _section_label(text: str, font_delta: int = 0) -> QLabel:
    lbl = QLabel(text)
    lbl.setFont(QFont("Helvetica Neue", 17 + font_delta, QFont.Weight.Bold))
    lbl.setStyleSheet(f"color: {C_SUB}; letter-spacing: 1px;")
    return lbl


# ─── Sidebar chapter item ─────────────────────────────────────────────────────

class ChapterItem(QWidget):
    def __init__(self, chapter: dict, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(2)

        available = chapter["status"] == "available"
        dot_color = C_GREEN if available else C_BORDER

        top = QHBoxLayout()
        self._num_lbl = QLabel("Introduction" if chapter['number'] == 0 else f"Chapter {chapter['number']}")
        self._num_lbl.setFont(QFont("Helvetica Neue", 18, QFont.Weight.Bold))
        self._num_lbl.setStyleSheet(f"color: {C_ACCENT if available else C_SUB};")

        self._dot = QLabel("●")
        self._dot.setStyleSheet(f"color: {dot_color}; font-size: 8px;")
        self._dot.setFixedWidth(14)

        top.addWidget(self._num_lbl)
        top.addStretch()
        top.addWidget(self._dot)

        self._title_lbl = QLabel(chapter["title"])
        self._title_lbl.setFont(QFont("Helvetica Neue", 20))
        self._title_lbl.setStyleSheet(f"color: {C_TEXT if available else C_SUB};")

        layout.addLayout(top)
        layout.addWidget(self._title_lbl)

    def mark_visited(self):
        self._dot.setStyleSheet(f"color: {C_SUB}; font-size: 8px;")

    def adjust_font(self, delta: int):
        for lbl in (self._num_lbl, self._title_lbl):
            f = lbl.font()
            f.setPointSize(max(8, f.pointSize() + delta))
            lbl.setFont(f)
        self.adjustSize()


# ─── GitHub icon & button ────────────────────────────────────────────────────

def _make_github_icon(size=20, color="#333333"):
    SVG_D = (
        "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385"
        ".6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724"
        "-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7"
        "c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236"
        " 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605"
        "-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22"
        "-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23"
        ".96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405"
        " 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176"
        ".765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92"
        ".42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286"
        " 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297"
        "c0-6.627-5.373-12-12-12"
    )
    path = QPainterPath()
    tokens = re.findall(
        r'[MmCcLlZz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?', SVG_D)
    i = 0
    cmd = None
    cx = cy = sx = sy = 0.0

    def nf():
        nonlocal i
        v = float(tokens[i]); i += 1; return v

    while i < len(tokens):
        if tokens[i] in 'MmCcLlZz':
            cmd = tokens[i]; i += 1; continue
        if cmd == 'M':
            x, y = nf(), nf(); path.moveTo(x, y); cx = x; cy = y; sx = x; sy = y; cmd = 'L'
        elif cmd == 'm':
            x = cx + nf(); y = cy + nf(); path.moveTo(x, y); cx = x; cy = y; sx = x; sy = y; cmd = 'l'
        elif cmd == 'L':
            x, y = nf(), nf(); path.lineTo(x, y); cx = x; cy = y
        elif cmd == 'l':
            x = cx + nf(); y = cy + nf(); path.lineTo(x, y); cx = x; cy = y
        elif cmd == 'C':
            x1, y1, x2, y2, x, y = nf(), nf(), nf(), nf(), nf(), nf()
            path.cubicTo(x1, y1, x2, y2, x, y); cx = x; cy = y
        elif cmd == 'c':
            x1 = cx + nf(); y1 = cy + nf()
            x2 = cx + nf(); y2 = cy + nf()
            x  = cx + nf(); y  = cy + nf()
            path.cubicTo(x1, y1, x2, y2, x, y); cx = x; cy = y
        elif cmd in 'Zz':
            path.closeSubpath(); cx = sx; cy = sy; cmd = None
        else:
            i += 1

    px = QPixmap(size, size)
    px.fill(Qt.GlobalColor.transparent)
    painter = QPainter(px)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.scale(size / 24.0, size / 24.0)
    painter.fillPath(path, QBrush(QColor(color)))
    painter.end()
    return QIcon(px)


class GitHubButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(26, 26)
        self.setIcon(_make_github_icon(14, "#333333"))
        self.setIconSize(QSize(14, 14))
        self.setToolTip("Git / GitHub")
        self.setStyleSheet(
            "QPushButton { background-color: white; border-radius: 13px; "
            "border: 1px solid #CCCCCC; }"
            "QPushButton:hover { background-color: #F0F0F0; }"
        )


# ─── GitHub dialogs ───────────────────────────────────────────────────────────

class GitInitDialog(QDialog):
    def __init__(self, creds, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Initialize & Create GitHub Repo")
        self.setMinimumWidth(460)
        self._result_creds = {}

        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form.setSpacing(10)

        self._user = QLineEdit(creds.get("username", ""))
        self._user.setPlaceholderText("your-github-username")

        pat_row = QHBoxLayout()
        self._pat = QLineEdit(creds.get("token", ""))
        self._pat.setEchoMode(QLineEdit.EchoMode.Password)
        self._pat.setPlaceholderText("ghp_xxxxxxxxxxxxxxxxxxxx")
        pat_help = QPushButton("?")
        pat_help.setFixedSize(22, 22)
        pat_help.setStyleSheet(
            "QPushButton { background: white; border-radius: 11px; "
            "border: 1px solid #ccc; font-weight: bold; font-size: 11px; color: #555; }"
            "QPushButton:hover { background: #f0f0f0; }"
        )
        pat_help.setToolTip("How to create a GitHub Personal Access Token")
        pat_help.clicked.connect(lambda: subprocess.Popen(
            ["open", "https://github.com/settings/tokens/new?description=PythonPlaybook&scopes=repo"]))
        pat_row.addWidget(self._pat)
        pat_row.addWidget(pat_help)

        self._repo = QLineEdit(creds.get("repo_name", ""))
        self._repo.setPlaceholderText("my-python-playbook")

        self._desc = QLineEdit(creds.get("description", ""))
        self._desc.setPlaceholderText("Optional description")

        form.addRow("GitHub Username:", self._user)
        form.addRow("Personal Access Token:", pat_row)
        form.addRow("Repository Name:", self._repo)
        form.addRow("Description:", self._desc)
        layout.addLayout(form)

        vis_row = QHBoxLayout()
        vis_label = QLabel("Visibility:")
        vis_label.setFixedWidth(140)
        vis_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self._pub_btn  = QPushButton("Public")
        self._priv_btn = QPushButton("Private")
        for btn in (self._pub_btn, self._priv_btn):
            btn.setCheckable(True)
            btn.setFixedWidth(90)
        self._pub_btn.setChecked(True)
        self._pub_btn.clicked.connect(lambda: self._set_vis(False))
        self._priv_btn.clicked.connect(lambda: self._set_vis(True))
        self._private = False
        self._update_vis_style()
        vis_row.addWidget(vis_label)
        vis_row.addWidget(self._pub_btn)
        vis_row.addWidget(self._priv_btn)
        vis_row.addStretch()
        layout.addLayout(vis_row)

        self._readme_cb = QCheckBox("Create README.md")
        self._readme_cb.setChecked(True)
        self._save_cb = QCheckBox("Save credentials for this session")
        self._save_cb.setChecked(creds.get("save", True))
        layout.addWidget(self._readme_cb)
        layout.addWidget(self._save_cb)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedWidth(90)
        cancel_btn.setStyleSheet(
            "QPushButton { padding: 8px; border-radius: 8px; border: 1px solid #ccc; }")
        cancel_btn.clicked.connect(self.reject)
        create_btn = QPushButton("Create")
        create_btn.setFixedWidth(90)
        create_btn.setStyleSheet(
            "QPushButton { background-color: #2DA44E; color: white; "
            "padding: 8px; border-radius: 8px; font-weight: bold; }"
            "QPushButton:hover { background-color: #218A41; }"
        )
        create_btn.clicked.connect(self._accept)
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(create_btn)
        layout.addLayout(btn_row)

    def _set_vis(self, private: bool):
        self._private = private
        self._pub_btn.setChecked(not private)
        self._priv_btn.setChecked(private)
        self._update_vis_style()

    def _update_vis_style(self):
        active   = "background-color: #0969DA; color: white; padding: 6px; border-radius: 6px; font-weight: bold;"
        inactive = "background-color: #f6f8fa; color: #333; padding: 6px; border-radius: 6px; border: 1px solid #ccc;"
        self._pub_btn.setStyleSheet(active if not self._private else inactive)
        self._priv_btn.setStyleSheet(active if self._private else inactive)

    def _accept(self):
        if not self._user.text().strip():
            QMessageBox.warning(self, "Missing Field", "GitHub Username is required."); return
        if not self._pat.text().strip():
            QMessageBox.warning(self, "Missing Field", "Personal Access Token is required."); return
        if not self._repo.text().strip():
            QMessageBox.warning(self, "Missing Field", "Repository Name is required."); return
        self._result_creds = {
            "username":    self._user.text().strip(),
            "token":       self._pat.text().strip(),
            "repo_name":   self._repo.text().strip(),
            "description": self._desc.text().strip(),
            "private":     self._private,
            "readme":      self._readme_cb.isChecked(),
            "save":        self._save_cb.isChecked(),
        }
        self.accept()

    def result_creds(self):
        return self._result_creds


class GitPushDialog(QDialog):
    def __init__(self, creds, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Commit & Push to GitHub")
        self.setMinimumWidth(460)
        self._result = {}

        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form.setSpacing(10)

        default_msg = f"Python Playbook update {time.strftime('%Y-%m-%d %H:%M')}"
        self._msg = QLineEdit(default_msg)

        saved_user = creds.get("username", "")
        saved_repo = creds.get("repo_name", "")
        default_repo_url = (
            f"https://github.com/{saved_user}/{saved_repo}"
            if saved_user and saved_repo else ""
        )
        self._repo_url = QLineEdit(default_repo_url)
        self._repo_url.setPlaceholderText("https://github.com/username/repo")

        pat_row = QHBoxLayout()
        self._pat = QLineEdit(creds.get("token", ""))
        self._pat.setEchoMode(QLineEdit.EchoMode.Password)
        self._pat.setPlaceholderText("ghp_xxxxxxxxxxxxxxxxxxxx")
        pat_help = QPushButton("?")
        pat_help.setFixedSize(22, 22)
        pat_help.setStyleSheet(
            "QPushButton { background: white; border-radius: 11px; "
            "border: 1px solid #ccc; font-weight: bold; font-size: 11px; color: #555; }"
            "QPushButton:hover { background: #f0f0f0; }"
        )
        pat_help.setToolTip("How to create a GitHub Personal Access Token")
        pat_help.clicked.connect(lambda: subprocess.Popen(
            ["open", "https://github.com/settings/tokens/new?description=PythonPlaybook&scopes=repo"]))
        pat_row.addWidget(self._pat)
        pat_row.addWidget(pat_help)

        self._branch = QComboBox()
        self._branch.addItems(["main", "roboapps"])
        saved_branch = creds.get("branch", "main")
        idx = self._branch.findText(saved_branch)
        self._branch.setCurrentIndex(idx if idx >= 0 else 0)

        form.addRow("Commit Message:", self._msg)
        form.addRow("GitHub Repository:", self._repo_url)
        form.addRow("Branch:", self._branch)
        form.addRow("Personal Access Token:", pat_row)
        layout.addLayout(form)

        self._save_cb = QCheckBox("Save credentials for this session")
        self._save_cb.setChecked(creds.get("save", True))
        layout.addWidget(self._save_cb)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedWidth(90)
        cancel_btn.setStyleSheet(
            "QPushButton { padding: 8px; border-radius: 8px; border: 1px solid #ccc; }")
        cancel_btn.clicked.connect(self.reject)
        push_btn = QPushButton("Push")
        push_btn.setFixedWidth(90)
        push_btn.setStyleSheet(
            "QPushButton { background-color: #0969DA; color: white; "
            "padding: 8px; border-radius: 8px; font-weight: bold; }"
            "QPushButton:hover { background-color: #0757BA; }"
        )
        push_btn.clicked.connect(self._accept)
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(push_btn)
        layout.addLayout(btn_row)

    def _accept(self):
        if not self._repo_url.text().strip():
            QMessageBox.warning(self, "Missing Field", "GitHub Repository URL is required."); return
        if not self._pat.text().strip():
            QMessageBox.warning(self, "Missing Field", "Personal Access Token is required."); return
        self._result = {
            "message":  self._msg.text().strip() or f"Python Playbook update {time.strftime('%Y-%m-%d %H:%M')}",
            "repo_url": self._repo_url.text().strip(),
            "branch":   self._branch.currentText(),
            "token":    self._pat.text().strip(),
            "save":     self._save_cb.isChecked(),
        }
        self.accept()

    def result_data(self):
        return self._result


class GitPullDialog(QDialog):
    def __init__(self, creds, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pull from GitHub")
        self.setMinimumWidth(320)
        self._result = {}

        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form.setSpacing(10)

        self._branch = QComboBox()
        self._branch.addItems(["main", "roboapps"])
        saved_branch = creds.get("branch", "main")
        idx = self._branch.findText(saved_branch)
        self._branch.setCurrentIndex(idx if idx >= 0 else 0)

        form.addRow("Branch:", self._branch)
        layout.addLayout(form)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedWidth(90)
        cancel_btn.setStyleSheet(
            "QPushButton { padding: 8px; border-radius: 8px; border: 1px solid #ccc; }")
        cancel_btn.clicked.connect(self.reject)
        pull_btn = QPushButton("Pull")
        pull_btn.setFixedWidth(90)
        pull_btn.setStyleSheet(
            "QPushButton { background-color: #0969DA; color: white; "
            "padding: 8px; border-radius: 8px; font-weight: bold; }"
            "QPushButton:hover { background-color: #0757BA; }"
        )
        pull_btn.clicked.connect(self._accept)
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(pull_btn)
        layout.addLayout(btn_row)

    def _accept(self):
        self._result = {"branch": self._branch.currentText()}
        self.accept()

    def result_data(self):
        return self._result


# ─── Main window ─────────────────────────────────────────────────────────────

class RobbyWindow(QMainWindow):
    _DRIVE_KEYS = {Qt.Key.Key_W, Qt.Key.Key_A, Qt.Key.Key_S, Qt.Key.Key_D}

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Playbook")
        self.resize(1100, 720)
        self._teacher_mode  = False
        self._current_index = 0
        self._build_ui()
        self._load_chapter(0)

    def keyPressEvent(self, event):
        if event.key() in self._DRIVE_KEYS:
            self._robosim_win.keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() in self._DRIVE_KEYS:
            self._robosim_win.keyReleaseEvent(event)
        else:
            super().keyReleaseEvent(event)

    def _build_ui(self):
        self.setStyleSheet(f"QMainWindow, QWidget#root {{ background: {C_BG}; }}")

        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)
        rl = QVBoxLayout(root)
        rl.setContentsMargins(0, 0, 0, 0)
        rl.setSpacing(0)

        # ── Toolbar ───────────────────────────────────────────────────────────
        tb = QWidget()
        tb.setFixedHeight(52)
        tb.setStyleSheet(f"background: {C_SIDEBAR}; border-bottom: 1px solid {C_BORDER};")
        tbl = QHBoxLayout(tb)
        tbl.setContentsMargins(12, 0, 20, 0)

        _tb_btn_style = "QPushButton { background: transparent; border: none; } QPushButton:hover { background: rgba(255,255,255,0.08); border-radius: 6px; }"

        icon_path = os.path.join(os.path.dirname(__file__), "icons", "sidebar_toggle.png")
        sidebar_btn = QPushButton()
        sidebar_btn.setIcon(QIcon(icon_path))
        sidebar_btn.setIconSize(QSize(21, 21))
        sidebar_btn.setFixedSize(29, 29)
        sidebar_btn.setStyleSheet(_tb_btn_style)
        sidebar_btn.setToolTip("Toggle sidebar")
        sidebar_btn.clicked.connect(self._toggle_sidebar)
        tbl.addWidget(sidebar_btn)

        self._git_btn = GitHubButton()
        self._git_btn.clicked.connect(self._show_git_menu)
        tbl.addWidget(self._git_btn)

        font_small_btn = QPushButton("A")
        font_small_btn.setFixedSize(29, 29)
        font_small_btn.setStyleSheet(_tb_btn_style + " QPushButton { font-size: 11px; color: white; }")
        font_small_btn.setToolTip("Decrease font size")
        font_small_btn.clicked.connect(lambda: self._adjust_all_fonts(-1))
        tbl.addWidget(font_small_btn)

        font_large_btn = QPushButton("A")
        font_large_btn.setFixedSize(29, 29)
        font_large_btn.setStyleSheet(_tb_btn_style + " QPushButton { font-size: 17px; color: white; font-weight: bold; }")
        font_large_btn.setToolTip("Increase font size")
        font_large_btn.clicked.connect(lambda: self._adjust_all_fonts(+1))
        tbl.addWidget(font_large_btn)

        tbl.addStretch()

        self._teacher_btn = QPushButton("Notes")
        self._teacher_btn.setCheckable(True)
        self._teacher_btn.setFixedHeight(32)
        self._teacher_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 0 16px; }")
        self._teacher_btn.clicked.connect(self._toggle_teacher_mode)
        tbl.addWidget(self._teacher_btn)


        rl.addWidget(tb)

        # ── Splitter ──────────────────────────────────────────────────────────
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setStyleSheet(f"QSplitter::handle {{ background: {C_BORDER}; width: 1px; }}")

        # Left sidebar
        sidebar = QWidget()
        sidebar.setMinimumWidth(210)
        sidebar.setMaximumWidth(260)
        sidebar.setStyleSheet(f"background: {C_SIDEBAR};")
        sl = QVBoxLayout(sidebar)
        sl.setContentsMargins(0, 8, 0, 8)
        sl.setSpacing(0)

        self._chapter_list = QListWidget()
        self._chapter_list.setStyleSheet(f"""
            QListWidget {{
                background: {C_SIDEBAR}; border: none; outline: none;
            }}
            QListWidget::item {{
                background: transparent;
                border-bottom: 1px solid {C_BORDER};
                padding: 0;
            }}
            QListWidget::item:selected {{ background: #3A3A3C; }}
            QListWidget::item:hover    {{ background: #333335; }}
        """)
        self._chapter_list.setSpacing(0)
        self._chapter_list.currentRowChanged.connect(self._on_chapter_changed)
        sl.addWidget(self._chapter_list)

        # Populate sidebar
        self._chapter_items = []
        for ch in CHAPTERS:
            item = QListWidgetItem()
            w = ChapterItem(ch)
            item.setSizeHint(w.sizeHint())
            if ch["status"] != "available":
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            self._chapter_list.addItem(item)
            self._chapter_list.setItemWidget(item, w)
            self._chapter_items.append(w)

        self._sidebar = sidebar
        splitter.addWidget(sidebar)

        # Right panel — nested splitter (chapter view | robosim)
        self._right_splitter = QSplitter(Qt.Orientation.Horizontal)
        self._right_splitter.setStyleSheet("QSplitter::handle { width: 0px; background: transparent; }")

        # Chapter container with header bar
        chapter_container = QWidget()
        chapter_container.setStyleSheet("background: transparent;")
        chapter_vl = QVBoxLayout(chapter_container)
        chapter_vl.setContentsMargins(0, 0, 0, 0)
        chapter_vl.setSpacing(0)

        chapter_header = QWidget()
        chapter_header.setFixedHeight(28)
        chapter_header.setStyleSheet(f"background: {C_SIDEBAR}; border-bottom: 1px solid {C_BORDER};")
        chapter_hl = QHBoxLayout(chapter_header)
        chapter_hl.setContentsMargins(4, 0, 4, 0)

        _ch_btn_style = ("QPushButton { background: transparent; border: none; color: white; font-size: 15px; }"
                         "QPushButton:hover { background: rgba(255,255,255,0.1); border-radius: 4px; }")

        self._chapter_exit_btn = QPushButton("✕")
        self._chapter_exit_btn.setFixedSize(24, 24)
        self._chapter_exit_btn.setStyleSheet(_ch_btn_style)
        self._chapter_exit_btn.setToolTip("Exit fullscreen")
        self._chapter_exit_btn.setVisible(False)
        self._chapter_exit_btn.clicked.connect(self._toggle_chapter_fullscreen)
        chapter_hl.addWidget(self._chapter_exit_btn)

        chapter_hl.addStretch()

        self._chapter_enlarge_btn = QPushButton("⛶")
        self._chapter_enlarge_btn.setFixedSize(24, 24)
        self._chapter_enlarge_btn.setStyleSheet(_ch_btn_style)
        self._chapter_enlarge_btn.setToolTip("Fullscreen chapter view")
        self._chapter_enlarge_btn.clicked.connect(self._toggle_chapter_fullscreen)
        chapter_hl.addWidget(self._chapter_enlarge_btn)

        chapter_vl.addWidget(chapter_header)

        self._chapter_view = ChapterView()
        chapter_vl.addWidget(self._chapter_view)

        self._chapter_container = chapter_container
        self._right_splitter.addWidget(self._chapter_container)

        # RoboSim container with header bar
        robosim_container = QWidget()
        robosim_container.setStyleSheet("background: transparent;")
        robosim_vl = QVBoxLayout(robosim_container)
        robosim_vl.setContentsMargins(0, 0, 0, 0)
        robosim_vl.setSpacing(0)

        robosim_header = QWidget()
        robosim_header.setFixedHeight(28)
        robosim_header.setStyleSheet(f"background: {C_SIDEBAR}; border-bottom: 1px solid {C_BORDER};")
        robosim_hl = QHBoxLayout(robosim_header)
        robosim_hl.setContentsMargins(4, 0, 4, 0)

        _rs_btn_style = ("QPushButton { background: transparent; border: none; color: white; font-size: 15px; }"
                         "QPushButton:hover { background: rgba(255,255,255,0.1); border-radius: 4px; }")

        self._robosim_exit_btn = QPushButton("✕")
        self._robosim_exit_btn.setFixedSize(24, 24)
        self._robosim_exit_btn.setStyleSheet(_rs_btn_style)
        self._robosim_exit_btn.setToolTip("Exit fullscreen")
        self._robosim_exit_btn.setVisible(False)
        self._robosim_exit_btn.clicked.connect(self._toggle_robosim_fullscreen)
        robosim_hl.addWidget(self._robosim_exit_btn)

        robosim_hl.addStretch()

        self._robosim_enlarge_btn = QPushButton("⛶")
        self._robosim_enlarge_btn.setFixedSize(24, 24)
        self._robosim_enlarge_btn.setStyleSheet(_rs_btn_style)
        self._robosim_enlarge_btn.setToolTip("Fullscreen RoboSim")
        self._robosim_enlarge_btn.clicked.connect(self._toggle_robosim_fullscreen)
        robosim_hl.addWidget(self._robosim_enlarge_btn)

        robosim_vl.addWidget(robosim_header)

        self._robosim_win = RoboSimWindow()
        self._robosim_win.mission_completed.connect(self._on_mission_complete)
        robosim_vl.addWidget(self._robosim_win)
        self._chapter_view.set_robosim(self._robosim_win)

        self._robosim_container = robosim_container
        self._right_splitter.addWidget(self._robosim_container)
        self._right_splitter.setSizes([435, 435])

        self._outer_splitter = splitter
        splitter.addWidget(self._right_splitter)
        splitter.setSizes([230, 870])

        rl.addWidget(splitter)

    def _load_chapter(self, index: int):
        self._current_index = index
        chapter = CHAPTERS[index]
        self._chapter_view.load(chapter, self._teacher_mode)
        self._chapter_list.blockSignals(True)
        self._chapter_list.setCurrentRow(index)
        self._chapter_list.blockSignals(False)
        self._chapter_items[index].mark_visited()
        wf = chapter.get("world_file", "")
        if wf:
            path = world_path(wf)
            if os.path.isfile(path):
                self._robosim_win.load_world(path)
        self._robosim_win.set_missions(chapter.get("missions", []))

    def _on_mission_complete(self, mission_num: int):
        self._chapter_view.mark_mission_done(mission_num)

    def _on_chapter_changed(self, row: int):
        if 0 <= row < len(CHAPTERS):
            self._load_chapter(row)

    def _toggle_sidebar(self):
        self._sidebar.setVisible(not self._sidebar.isVisible())

    def _toggle_robosim_fullscreen(self):
        entering = not getattr(self, "_robosim_fullscreen", False)
        if entering:
            self._rs_fs_outer = self._outer_splitter.sizes()
            self._rs_fs_right = self._right_splitter.sizes()
            self._sidebar.setVisible(False)
            self._chapter_container.setVisible(False)
            self._robosim_enlarge_btn.setVisible(False)
            self._robosim_exit_btn.setVisible(True)
        else:
            self._sidebar.setVisible(True)
            self._chapter_container.setVisible(True)
            self._robosim_exit_btn.setVisible(False)
            self._robosim_enlarge_btn.setVisible(True)
            if hasattr(self, "_rs_fs_right"):
                self._right_splitter.setSizes(self._rs_fs_right)
            if hasattr(self, "_rs_fs_outer"):
                self._outer_splitter.setSizes(self._rs_fs_outer)
        self._robosim_fullscreen = entering

    def _toggle_chapter_fullscreen(self):
        entering = not getattr(self, "_chapter_fullscreen", False)
        if entering:
            self._ch_fs_outer = self._outer_splitter.sizes()
            self._ch_fs_right = self._right_splitter.sizes()
            self._sidebar.setVisible(False)
            self._robosim_container.setVisible(False)
            self._chapter_enlarge_btn.setVisible(False)
            self._chapter_exit_btn.setVisible(True)
        else:
            self._sidebar.setVisible(True)
            self._robosim_container.setVisible(True)
            self._chapter_exit_btn.setVisible(False)
            self._chapter_enlarge_btn.setVisible(True)
            if hasattr(self, "_ch_fs_right"):
                self._right_splitter.setSizes(self._ch_fs_right)
            if hasattr(self, "_ch_fs_outer"):
                self._outer_splitter.setSizes(self._ch_fs_outer)
        self._chapter_fullscreen = entering

    def _adjust_all_fonts(self, delta: int):
        self._chapter_view.adjust_font(delta)
        for i in range(self._chapter_list.count()):
            w = self._chapter_list.itemWidget(self._chapter_list.item(i))
            if isinstance(w, ChapterItem):
                w.adjust_font(delta)
                self._chapter_list.item(i).setSizeHint(w.sizeHint())

    def _toggle_teacher_mode(self):
        self._teacher_mode = self._teacher_btn.isChecked()
        if self._teacher_mode:
            self._teacher_btn.setStyleSheet(
                _BTN_GREY
                + f"QPushButton {{ padding: 0 16px; color: {C_GREEN}; border: 1px solid {C_GREEN}; }}"
            )
        else:
            self._teacher_btn.setStyleSheet(_BTN_GREY + "QPushButton { padding: 0 16px; }")
        self._chapter_view.set_teacher_mode(self._teacher_mode)

    # ── Git / GitHub ──────────────────────────────────────────────────────────

    def _load_git_creds(self):
        try:
            with open(_GIT_CREDS_FILE, "r") as fh:
                return json.load(fh)
        except Exception:
            return {}

    def _save_git_creds(self, creds: dict):
        try:
            existing = self._load_git_creds()
            existing.update(creds)
            with open(_GIT_CREDS_FILE, "w") as fh:
                json.dump(existing, fh, indent=2)
        except Exception:
            pass

    def _show_git_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet(
            "QMenu { background: white; border: 1px solid #ddd; border-radius: 8px; "
            "padding: 4px 0; font-size: 13px; }"
            "QMenu::item { padding: 8px 24px; color: #1a1a1a; }"
            "QMenu::item:selected { background: #F0F0F0; color: #1a1a1a; border-radius: 4px; }"
            "QMenu::separator { height: 1px; background: #eee; margin: 4px 0; }"
        )
        init_action = menu.addAction("  Create GitHub Repo")
        push_action = menu.addAction("  Commit & Push")
        pull_action = menu.addAction("  Pull from GitHub")
        menu.addSeparator()
        menu.addAction("  Cancel")

        btn_pos = self._git_btn.mapToGlobal(self._git_btn.rect().bottomLeft())
        chosen  = menu.exec(btn_pos)

        if chosen == init_action:
            self._git_init()
        elif chosen == push_action:
            self._git_push()
        elif chosen == pull_action:
            self._git_pull()

    def _git_init(self):
        creds  = self._load_git_creds()
        dialog = GitInitDialog(creds, parent=self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        data = dialog.result_creds()

        if data.get("save"):
            self._save_git_creds({
                "username":    data["username"],
                "token":       data["token"],
                "repo_name":   data["repo_name"],
                "description": data["description"],
                "save":        True,
            })

        errors = []

        r = subprocess.run(["git", "init"], cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"git init failed:\n{r.stderr.strip()}")

        subprocess.run(["git", "config", "user.name",  data["username"]], cwd=_APP_DIR)
        subprocess.run(["git", "config", "user.email",
                        f"{data['username']}@users.noreply.github.com"], cwd=_APP_DIR)

        gitignore = os.path.join(_APP_DIR, ".gitignore")
        hidden = {".git_credentials.json", "__pycache__/", "*.pyc", ".DS_Store"}
        try:
            existing_lines = open(gitignore).read().splitlines() if os.path.exists(gitignore) else []
            with open(gitignore, "a") as fh:
                for entry in hidden:
                    if entry not in existing_lines:
                        fh.write(entry + "\n")
        except Exception:
            pass

        if data["readme"]:
            readme_path = os.path.join(_APP_DIR, "README.md")
            if not os.path.exists(readme_path):
                try:
                    with open(readme_path, "w") as fh:
                        fh.write(f"# {data['repo_name']}\n\n{data['description']}\n")
                except Exception:
                    pass

        try:
            payload = json.dumps({
                "name":        data["repo_name"],
                "description": data["description"],
                "private":     data["private"],
                "auto_init":   False,
            }).encode()
            req = urllib.request.Request(
                "https://api.github.com/user/repos",
                data=payload,
                headers={
                    "Authorization": f"token {data['token']}",
                    "Content-Type":  "application/json",
                    "Accept":        "application/vnd.github+json",
                    "User-Agent":    "PythonPlaybook-App",
                },
                method="POST",
            )
            with urllib.request.urlopen(req) as resp:
                repo_info = json.loads(resp.read())
            clone_url = repo_info.get("clone_url", "")
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            errors.append(f"GitHub API error {e.code}:\n{body[:300]}")
            clone_url = ""
        except Exception as e:
            errors.append(f"GitHub API error: {e}")
            clone_url = ""

        if clone_url:
            auth_url = clone_url.replace(
                "https://", f"https://{data['username']}:{data['token']}@")
            subprocess.run(["git", "remote", "remove", "origin"],
                           cwd=_APP_DIR, capture_output=True)
            subprocess.run(["git", "remote", "add", "origin", auth_url],
                           cwd=_APP_DIR, capture_output=True)

        subprocess.run(["git", "add", "."], cwd=_APP_DIR, capture_output=True)
        r = subprocess.run(["git", "commit", "-m", "Initial commit — Python Playbook"],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0 and "nothing to commit" not in r.stdout:
            errors.append(f"git commit failed:\n{r.stderr.strip()}")

        if clone_url:
            r = subprocess.run(["git", "push", "-u", "origin", "HEAD"],
                               cwd=_APP_DIR, capture_output=True, text=True)
            if r.returncode != 0:
                errors.append(f"git push failed:\n{r.stderr.strip()}")

        if errors:
            QMessageBox.warning(self, "Git — Issues Encountered", "\n\n".join(errors))
        else:
            repo_url = f"https://github.com/{data['username']}/{data['repo_name']}"
            QMessageBox.information(self, "Git — Repository Created",
                                    f"Repository created and initial push complete.\n\n{repo_url}")

    def _git_push(self):
        r = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            QMessageBox.warning(self, "Git — Not Initialised",
                                "This project is not a git repository yet.\n"
                                "Use 'Create GitHub Repo' first.")
            return
        creds  = self._load_git_creds()
        dialog = GitPushDialog(creds, parent=self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        data = dialog.result_data()

        if data.get("save"):
            m = re.match(r'https://github\.com/([^/]+)/([^/]+?)(?:\.git)?$', data["repo_url"])
            update = {"token": data["token"], "branch": data["branch"]}
            if m:
                update["username"] = m.group(1)
                update["repo_name"] = m.group(2)
            self._save_git_creds(update)

        errors = []
        branch = data.get("branch", "main")

        auth_url = data["repo_url"]
        m = re.match(r'https://github\.com/([^/]+)', data["repo_url"])
        if m:
            auth_url = data["repo_url"].replace(
                "https://", f"https://{m.group(1)}:{data['token']}@")

        subprocess.run(["git", "remote", "remove", "origin"],
                       cwd=_APP_DIR, capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", auth_url],
                       cwd=_APP_DIR, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=_APP_DIR, capture_output=True)

        r = subprocess.run(["git", "commit", "-m", data["message"]],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0 and "nothing to commit" not in r.stdout and "nothing to commit" not in r.stderr:
            errors.append(f"git commit: {r.stderr.strip() or r.stdout.strip()}")

        r = subprocess.run(["git", "pull", "--rebase", "origin", branch],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"git pull --rebase failed:\n{r.stderr.strip() or r.stdout.strip()}")

        r = subprocess.run(["git", "push", "-u", "origin", f"HEAD:{branch}"],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"git push failed:\n{r.stderr.strip()}")

        if errors:
            QMessageBox.warning(self, "Git — Push Issues", "\n\n".join(errors))
        else:
            QMessageBox.information(self, "Git — Push Complete",
                                    f"Successful push to:\n{data['repo_url']}  [{branch}]")

    def _git_pull(self):
        creds = self._load_git_creds()
        r = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            QMessageBox.warning(self, "Git — Not Initialised",
                                "This project is not a git repository yet.\n"
                                "Use 'Create GitHub Repo' first.")
            return

        dlg = GitPullDialog(creds, self)
        if dlg.exec() != QDialog.DialogCode.Accepted:
            return
        data = dlg.result_data()
        branch = data["branch"]
        token  = creds.get("token", "")

        if token:
            r2 = subprocess.run(["git", "remote", "get-url", "origin"],
                                cwd=_APP_DIR, capture_output=True, text=True)
            remote_url = r2.stdout.strip()
            if remote_url and "github.com" in remote_url:
                m = re.match(r'https://github\.com/([^/]+)', remote_url)
                if m:
                    auth_url = remote_url.replace(
                        "https://", f"https://{m.group(1)}:{token}@")
                    subprocess.run(["git", "remote", "set-url", "origin", auth_url],
                                   cwd=_APP_DIR, capture_output=True)

        r = subprocess.run(["git", "pull", "--rebase", "origin", branch],
                           cwd=_APP_DIR, capture_output=True, text=True)
        if r.returncode != 0:
            QMessageBox.warning(self, "Git — Pull Failed", r.stderr.strip())
        else:
            r2 = subprocess.run(["git", "remote", "get-url", "origin"],
                                cwd=_APP_DIR, capture_output=True, text=True)
            clean_url = re.sub(r'https://[^@]+@', 'https://', r2.stdout.strip())
            QMessageBox.information(self, "Git — Pull Complete",
                                    f"Successful pull from:\n{clean_url}  [{branch}]")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Python Playbook")
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window,          QColor(C_BG))
    palette.setColor(QPalette.ColorRole.WindowText,      QColor(C_TEXT))
    palette.setColor(QPalette.ColorRole.Base,            QColor(C_SIDEBAR))
    palette.setColor(QPalette.ColorRole.AlternateBase,   QColor("#3A3A3C"))
    palette.setColor(QPalette.ColorRole.Text,            QColor(C_TEXT))
    palette.setColor(QPalette.ColorRole.Button,          QColor("#3A3A3C"))
    palette.setColor(QPalette.ColorRole.ButtonText,      QColor(C_TEXT))
    palette.setColor(QPalette.ColorRole.Highlight,       QColor(C_ACCENT))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#FFFFFF"))
    app.setPalette(palette)

    win = RobbyWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
