import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import requests

    url = "https://api.riksbank.se/swea/v1/Observations/SEKUSDPMI/2020-01-01"

    df = pl.read_json(requests.get(url).content, schema={"date": pl.String, "value": pl.Float64})
    df = df.with_columns(pl.col('date').cast(pl.Date))
    df
    return


if __name__ == "__main__":
    app.run()
