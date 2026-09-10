"""OGP カード画像（1200x630）を生成する。

出力先: ../og/*.png
実行:   python tools/make_og_images.py

サイトの配色（wave=#0088aa / quantum=#6d28d9 / modular=#15803d）に合わせ、
論文名・英語サブタイトル・arXiv ID を載せた言語非依存のカードを作る。
日本語フォントは Meiryo、英数字は Consolas を使う。
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = Path(__file__).resolve().parent.parent / "og"

BG = (255, 255, 255)
INK = (16, 23, 40)
MUTED = (65, 74, 99)
DIM = (107, 117, 145)
RULE = (211, 216, 234)

WAVE = (0, 136, 170)
QUANTUM = (109, 40, 217)
MODULAR = (21, 128, 61)

SERIF = "C:/Windows/Fonts/meiryo.ttc"
MONO = "C:/Windows/Fonts/consola.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def card(name: str, accent, kicker: str, title: str, subtitle: list[str],
         footer: str, title_size: int = 84) -> None:
    """1枚のカードを描いて png として保存する。"""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # 上端のアクセントバー
    d.rectangle([0, 0, W, 10], fill=accent)

    # 左の細いルール（本文の縦位置を揃える基準線）
    x = 90
    d.line([(x, 150), (x, H - 150)], fill=RULE, width=2)

    tx = x + 42
    d.text((tx, 150), kicker, font=font(MONO, 22), fill=accent)

    y = 200
    d.text((tx, y), title, font=font(SERIF, title_size), fill=INK,
           stroke_width=1, stroke_fill=INK)

    y += title_size + 40
    for line in subtitle:
        d.text((tx, y), line, font=font(SERIF, 27), fill=MUTED)
        y += 44

    d.line([(tx, H - 132), (W - 90, H - 132)], fill=RULE, width=1)
    d.text((tx, H - 112), footer, font=font(MONO, 24), fill=DIM)

    OUT.mkdir(exist_ok=True)
    path = OUT / f"og-{name}.png"
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path.name}")


def main() -> None:
    card(
        "index", INK,
        "KASUBUCHI & FUKIYA — PAPER EXPLAINERS",
        "論文解説ページ",
        ["WavePhaseNet ／ QuantumPhaseNet ／ ModularPhaseNet",
         "大規模言語モデルの幻覚を、意味の周波数構造と幾何学から扱う3本の論文。"],
        "kasubuchi.github.io/wavephasenet",
    )

    card(
        "modular", MODULAR,
        "ARXIV:2609.06000 — PAPER EXPLAINER",
        "ModularPhaseNet",
        ["Finite-Cyclic Phase Geometry for Computable Semantic Hierarchy,",
         "Direction, and Context Consistency in Standard Transformers"],
        "arXiv:2609.06000 · kasubuchi.github.io/wavephasenet",
    )

    card(
        "quantum", QUANTUM,
        "ARXIV:2608.15820 — PAPER EXPLAINER",
        "QuantumPhaseNet",
        ["A Gauge-Covariant Geometric and Quantum-Spectral Theory",
         "of Semantic Concept Hierarchies"],
        "arXiv:2608.15820 · kasubuchi.github.io/wavephasenet",
    )

    card(
        "wave", WAVE,
        "ARXIV:2602.14419 — PAPER EXPLAINER",
        "WavePhaseNet",
        ["A DFT-Based Method for Constructing Semantic",
         "Conceptual Hierarchy Structures (SCHS)"],
        "arXiv:2602.14419 · kasubuchi.github.io/wavephasenet",
    )

    card(
        "relation", INK,
        "HOW THE THREE PAPERS RELATE",
        "3つの論文の関係",
        ["連続なフーリエ位相 → ゲージ共変な複素幾何 → 有限巡回群。",
         "何が変わり、何が引き継がれなかったのかを整理しています。"],
        "kasubuchi.github.io/wavephasenet",
        title_size=72,
    )


if __name__ == "__main__":
    main()
