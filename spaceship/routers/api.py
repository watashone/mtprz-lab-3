from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/matrix")
def matrix_mult():
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    return {
        "matrix_a": a.tolist(),
        "matrix_b": b.tolist(),
        "product": (a @ b).tolist()
    }