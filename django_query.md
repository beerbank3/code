# django DB Query

1. filter
<code>
```
Model.objects.filter(조건)
```
</code>

<code>
```
from myapp.models import Book

# 제목이 'Django for Beginners'인 책 검색
books = Book.objects.filter(title='Django for Beginners')

# 저자가 'John Smith'인 책 검색
books = Book.objects.filter(author='John Smith')
```
</code>


