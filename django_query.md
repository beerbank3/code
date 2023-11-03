# django DB Query

## QuerySet

```
from myapp.models import MyModel

queryset = MyModel.objects.all()
```
- MyModel 모델에서 모든 레코드를 가져와서 QuerySet을 생성

1. 필터링:
- filter() 메서드를 사용하여 특정 조건을 만족하는 레코드를 검색할 수 있습니다.
```
Model.objects.filter(조건)
```

```
filtered_queryset = MyModel.objects.filter(field_name=value)
```

- MyModel 모델에서 name 필드가 "John"인 레코드를 검색하려면 다음과 같이 사용할 수 있습니다
```
filtered_queryset = MyModel.objects.filter(name="John")
```

2. 정렬
- order_by() 메서드를 사용하여 결과를 특정 필드를 기준으로 정렬할 수 있습니다.

```
sorted_queryset = MyModel.objects.order_by('field_name')
```
- MyModel 모델에서 age 필드를 기준으로 정렬하려면 다음과 같이 사용할 수 있습니다
```
sorted_queryset = MyModel.objects.order_by('age')
```

3. 값 추출
- values() 메서드를 사용하여 특정 필드의 값만 가져올 수 있습니다.

```
values_queryset = MyModel.objects.values('field_name')
```
- MyModel 모델에서 name 필드의 값을 가져오려면 다음과 같이 사용할 수 있습니다:
```
values_queryset = MyModel.objects.values('name')
```
4. 조인:
- select_related() 및 prefetch_related() 메서드를 사용하여 관련된 모델을 미리 로드할 수 있습니다. 이를 통해 N+1 쿼리 문제를 해결할 수 있습니다.

```
queryset = MyModel.objects.select_related('related_model')
```
- MyModel과 related_model 간의 관계를 가진 모델을 검색하고 관련된 모델을 미리 로드합니다.

```
from myapp.models import Book

# 책을 검색하고 해당 책의 저자 정보를 미리 로드
books = Book.objects.select_related('author')

# 이제 books QuerySet에는 책과 관련된 저자 정보가 미리 로드되어 있음
for book in books:
    print(f"책 제목: {book.title}")
    print(f"저자: {book.author.name}")

```

5. values_list
- 데이터베이스에서 검색한 결과를 튜플의 리스트로 반환하는 메서드입니다. 

```
QuerySet.values_list(*fields, flat=False)
```

- fields (필수): 반환할 필드 이름을 나타내는 위치 인자입니다. 여러 필드를 나열할 수 있으며, 튜플의 형태로 반환됩니다.
- flat (선택적): True로 설정하면 결과를 평평한 리스트(단일 값 리스트)로 반환하며, False로 설정하면 결과를 튜플의 리스트로 반환합니다. 기본값은 False입니다.

- 필드 하나만 추출
```
from myapp.models import Book

# Book 모델에서 title 필드만 추출
titles = Book.objects.values_list('title', flat=True)

# 결과를 리스트로 반환
print(list(titles))
```

- 필드 여러개 추출
```
from myapp.models import Book

# Book 모델에서 title과 author 필드를 추출
data = Book.objects.values_list('title', 'author')

# 결과를 리스트로 반환
print(list(data))
```
