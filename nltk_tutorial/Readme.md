## Edit the nltk_data path
To modify the path, simply append to the list of possible paths:
```python
import nltk
nltk.data.path.append("/home/yourusername/path/")
```
Or in windows:
```python
import nltk
nltk.data.path.append("C:\somewhere\path")
```