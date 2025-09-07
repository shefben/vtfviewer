# VTF Viewer (Python)

This project provides a pure Python implementation of a VTF (Valve Texture Format) viewer. It replaces the original C/SDL/OpenGL implementation with portable Python code that has no external C dependencies.

## Features

- Parses VTF headers and image data.
- Supports uncompressed formats and DXT1/DXT5 textures (including alpha for DXT5).
- Simple Tkinter viewer to browse frames and animate sequences.

## Usage

```bash
python viewer.py <path/to/file.vtf> [more.vtf ...]
```

Controls:

- `J` / `K` – navigate between provided files.
- `A` – play animation for the current file.
- Any other key – stop animation.

## License

This code is provided as-is under the original project's license.
