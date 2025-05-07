import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    1+1
    return


if __name__ == "__main__":
    app.run()
