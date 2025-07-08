# How to convert docs to Jupyter notebooks

- Install pandoc:
  - `conda install pandoc`
  - or `pip install pandoc`
- Then edit the path in [convert.py](convert.py) and run it. All `.rst` files in the folder will be converted.
- Or do it manually:
  - `pandoc [input.rst] -o [output.ipynb] --from rst --to ipynb`

Conclusion: pandoc doesn't work well.
