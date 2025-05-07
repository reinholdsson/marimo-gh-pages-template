import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    from urllib.request import Request, urlopen

    req = Request(
        url='https://www.riksbank.se/globalassets/media/statistik/iris/statistik-for-svenska-bankgrupper.xlsx', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    df = pl.read_excel(urlopen(req).read(), sheet_name="Immediate counterparty")

    df.head()
    return


if __name__ == "__main__":
    app.run()
