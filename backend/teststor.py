# test_storage.py
from storage import save_token, get_all_tokens

save_token("dummy_token_123")
print("✅ Tokens now:", get_all_tokens())
