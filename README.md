Установите все зависимости. Рекомендуется Python3.10
```cli
pip install -r requirments.txt
```
git config filter.strip-notebook-output.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR'