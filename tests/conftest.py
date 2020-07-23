import os


from pytest import fixture


@fixture
def printer():
    from litex.novitus import Printer

    return Printer(
        os.environ['NOVITUS_URL'],
        crc=True
    )
