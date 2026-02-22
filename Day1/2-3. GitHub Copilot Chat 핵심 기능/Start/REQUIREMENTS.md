# UserManager 개선 요구사항

## 배경

기존 UserManager 클래스를 보안, 성능, 기능 측면에서 개선해야 합니다.

## 요구사항

### 1. 검증 강화
- **username**: 3-20자, 알파벳과 숫자만 허용
- **email**: 유효한 이메일 형식 검증 (예: user@example.com)
- **age**: 18-120 범위 검증

### 2. remove_user 메서드 구현
- username으로 사용자 찾기
- 사용자 없으면 False 반환
- 사용자 있으면 제거 후 True 반환

### 3. 예외 처리 추가
- username이 이미 존재하면 `DuplicateUserError` 발생
- 검증 실패하면 `ValidationError` 발생
- 각 예외에 명확한 메시지 제공

### 4. 성능 개선
- username으로 빠른 조회 가능하도록 dict 사용
- 기존 `find_user()` 메서드는 O(n)에서 O(1)로 개선
- 대규모 사용자 데이터 처리 시 성능 보장

### 5. 기능 추가 (선택)
- 사용자 업데이트 메서드: `update_user(username, **kwargs)`
- 모든 사용자 조회 시 정렬 옵션: `get_all_users(sort_by='username')`

## 테스트 기준

구현 후 다음을 확인하세요:

```python
# 검증 테스트
- validate()가 유효한 username, email, age만 수락
- 짧은 username (1-2자) 거절
- 잘못된 이메일 형식 거절
- 범위 밖의 age 거절

# 추가/제거 테스트
- 중복 username 시 DuplicateUserError 발생
- remove_user()가 올바르게 제거
- 없는 사용자 제거 시 False 반환

# 성능 테스트
- 1000명 이상의 사용자 추가 및 조회 가능
- find_user()의 빠른 응답
```

## 우선순위

1. **필수**: 검증 강화, remove_user 구현, 기본 예외 처리
2. **권장**: dict 기반 성능 개선
3. **선택**: 추가 기능

---