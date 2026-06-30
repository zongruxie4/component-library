import os

def test_iterate2( ):
    # Note: the metric (yval) is declared in the 'metrics:' section of the
    # HPO YAML; the iterate2 CLI no longer takes --metric / --root-dir /
    # --wlm / --gpu-count / --cpu-count / --mem-gb (removed in the refactor).
    script = """
iterate \
  --script ./examples/bumpy_function.py \
  --optuna-study-name hpo \
  --optuna-db-path "sqlite:///iterate_study.db" \
  --hpo-yaml examples/bumpy_hpo.yaml \
  --optuna-n-trials 10
    """
    ret = os.system(script)
    assert ret == 0