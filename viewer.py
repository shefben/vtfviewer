"""Simple Tkinter-based VTF viewer."""
from __future__ import annotations

import base64
import sys
import tkinter as tk
from typing import List

from vtf import VTFFile


def _rgba_to_photoimage(w: int, h: int, rgba: bytes) -> tk.PhotoImage:
    header = f"P6 {w} {h} 255\n".encode()
    body = bytearray()
    for i in range(0, len(rgba), 4):
        body.extend(rgba[i : i + 3])
    data = base64.b64encode(header + body)
    return tk.PhotoImage(data=data)


class Viewer:
    def __init__(self, paths: List[str]):
        self.paths = paths
        self.idx = 0
        self.vtf = None
        self.root = tk.Tk()
        self.root.bind("<Key>", self.on_key)
        self.label = tk.Label(self.root)
        self.label.pack()
        self.load_file(0)

    def load_file(self, idx: int):
        self.vtf = VTFFile(self.paths[idx])
        self.frame = 0
        self.animate = False
        self.show_frame()

    def show_frame(self):
        w, h, pixels = self.vtf.get_image(self.frame)
        photo = _rgba_to_photoimage(w, h, pixels)
        self.label.configure(image=photo)
        self.label.image = photo
        self.root.title(f"{self.paths[self.idx]} (frame {self.frame+1}/{self.vtf.frame_count})")

    def on_key(self, event):
        ch = event.keysym.lower()
        if ch == 'j':
            self.idx = (self.idx + 1) % len(self.paths)
            self.load_file(self.idx)
        elif ch == 'k':
            self.idx = (self.idx - 1) % len(self.paths)
            self.load_file(self.idx)
        elif ch == 'a':
            self.animate = True
            self.frame = 0
            self.root.after(0, self.next_frame)
        else:
            self.animate = False

    def next_frame(self):
        if not self.animate:
            return
        self.show_frame()
        self.frame = (self.frame + 1) % self.vtf.frame_count
        self.root.after(100, self.next_frame)

    def run(self):
        self.root.mainloop()


def main(argv: List[str]):
    if len(argv) < 2:
        print("Usage: viewer.py <vtf files>")
        return 1
    Viewer(argv[1:]).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
