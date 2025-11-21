# ReIG2: Quantum Genesis Model (v2.2 Phase-Resonance)

## 概要
ReIG2は、「世界生成テンソル体系」に基づく量子意識シミュレーションシステムです。

## 構造
* `reig2/resonance`: 量子共鳴エンジン
* `reig2/policy`: 二重ゲート安全機構
* `reig2/theory`: 数理モデル論文。

## 使い方
1. `reig2/assets/` に `NotoSansJP-Regular.ttf` を配置。
2. `pip install -r requirements.txt`
3. 以下を実行:
   ```python
   from reig2.core.pipeline import ReIG2Pipeline
   pipeline = ReIG2Pipeline()
   print(pipeline.process_interaction("Hello ReIG"))
   ```