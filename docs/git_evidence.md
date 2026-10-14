# Git evidence

## `git log --oneline --graph --all --decorate`

```text
* e2c22ba (HEAD -> main) docs(discount): record experimental threshold note
* a834ceb fix(core): apply critical patch
| * de8ac83 (hotfix/patch) fix(core): apply critical patch
|/
*   e72ea98 (tag: v1.0.0) merge: integrate feature/payment
|\
| * 8574470 (feature/payment) feat(payment): implement payment contract
|/
* 55a0f1d feat(order): implement clean architecture service
```

## `git tag -n`

```text
v1.0.0          release: version 1.0.0
```

## `python -m unittest discover -s tests -v`

```text
test_create_order_saves_to_memory_repository ... ok
test_sqlite_repository_restores_order ... ok
test_empty_order_is_rejected ... ok
test_invalid_quantity_is_rejected ... ok
test_order_discount_applied ... ok
test_order_without_discount ... ok

Ran 6 tests

OK
```

