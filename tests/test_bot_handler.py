import unittest
import importlib
import sys
import types
from unittest import mock

import contact.ui.default_config as config


class BotHandlerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        sys.modules.setdefault(
            "contact.message_handlers.tx_handler",
            types.SimpleNamespace(send_message=mock.Mock()),
        )
        cls.bot_handler = importlib.import_module("contact.message_handlers.bot_handler")

    def test_is_bot_message_uses_configured_catch_words(self) -> None:
        with mock.patch.object(config, "ping_bot_catch_words", "ping; test; pong"):
            self.assertTrue(self.bot_handler.is_bot_message("PING"))
            self.assertTrue(self.bot_handler.is_bot_message("test"))
            self.assertFalse(self.bot_handler.is_bot_message("hello"))

    def test_is_bot_message_ignores_empty_config_values(self) -> None:
        with mock.patch.object(config, "ping_bot_catch_words", " ;  ; "):
            self.assertTrue(self.bot_handler.is_bot_message("ping"))


if __name__ == "__main__":
    unittest.main()
