from src.app.model import Model


def test_predict_simple():
    m = Model()
    out = m.predict([1.0, 2.0, 3.0])
    assert isinstance(out, list)
    assert abs(sum(out) - 1.0) < 1e-6
