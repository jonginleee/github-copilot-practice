from __future__ import annotations
from dataclasses import dataclass

class InsufficientFunds(Exception):
    pass

@dataclass(frozen=True)
class Transaction:
    kind: str   # "deposit" | "withdraw"
    amount: int
    balance_after: int

class BankAccount:
    def __init__(self, owner: str, initial_balance: int = 0) -> None:
        if initial_balance < 0:
            raise ValueError("initial_balance must be >= 0")
        self.owner = owner
        self._balance = initial_balance
        self.ledger: list[Transaction] = []

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        raise NotImplementedError

    def statement(self) -> str:
        """
        사람이 읽을 수 있는 거래 내역을 반환한다.
        예:
        deposit  +1000  balance=1000
        withdraw  -250  balance=750
        """
        raise NotImplementedError
