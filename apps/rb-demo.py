import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Demo

    Data is downloaded from, haven't yet solved how to read directly from url using pyodide:

    https://www.riksbank.se/sv/statistik/rapportering-av-internationell-bankstatistik-iris/svenska-bankgrupper/
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Below is a table of data:""")
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl

    # example from rb webpage
    url = str(mo.notebook_location() / "public" / "statistik-for-svenska-bankgrupper.xlsx")
    df = pl.read_excel(url, sheet_name="Immediate counterparty")
    df.head()
    return (mo,)


if __name__ == "__main__":
    app.run()
