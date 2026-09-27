from .engine import StreamEngine

def health(engine: StreamEngine) -> dict[str, int | bool]:
    stats = engine.stats()
    return {"accepted": stats.accepted, "late": stats.rejected_late, "watermark": stats.watermark, "healthy": stats.rejected_late == 0}
