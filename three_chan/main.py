import uvicorn

from three_chan.common.setup import setup_app

if __name__ == "__main__":
    app = setup_app()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
