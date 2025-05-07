import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium", layout_file="layouts/rb-demo.grid.json")


@app.cell
async def _():
    # required for WASM notebooks
    import micropip
    await micropip.install("openpyxl")
    return


@app.cell
def _(mo):
    mo.md(r"""## Demo""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    /// admonition | Note.

    This is only an example plot for demo purpose. See [here](https://www.riksbank.se/sv/statistik/rapportering-av-internationell-bankstatistik-iris/svenska-bankgrupper/) for more info about the data.
    ///
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
    df = pl.read_excel(url, sheet_name="Immediate counterparty", engine="openpyxl")
    #df
    return df, mo, pl


@app.cell
def _(df, mo):
    ref_vals = df.get_column("Reference Period").sort().to_list()
    ref_period = mo.ui.dropdown(value=max(ref_vals), options=ref_vals, label="Reference period", allow_select_none=False)
    ref_period
    return (ref_period,)


@app.cell
def _(df, mo, pl, ref_period):
    import altair as alt

    df_agg = df.filter(
        pl.col("Reference Period") == ref_period.value,
        pl.col("Counterparty Country").str.len_chars() == 2,
        ~pl.col("Counterparty Country").is_in(["SE"])
    ).group_by("Counterparty Country").agg(pl.col("Amount in MSEK").sum()).sort("Amount in MSEK", descending=True).head(10)

    chart = mo.ui.altair_chart(alt.Chart(df_agg).mark_bar().encode(
        alt.X('Amount in MSEK'),
        #y='Counterparty Country',
        alt.Y('Counterparty Country').sort('-x')
    ))
    chart

    return chart, df_agg


@app.cell
def _(chart, df_agg):
    if len(chart.value) == 0:
        res = df_agg
    else:
        res = chart.value.head()
    res
    return


if __name__ == "__main__":
    app.run()
