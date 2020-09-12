import asyncio
import commands
import random
import unittest

from test.shared import async_mock
from unittest import mock


class RollCommandTest(unittest.TestCase):
    @mock.patch('random.randint', return_value=20)
    def test_basic_command(self, mock_randint):
        mock_cmdio = async_mock.AsyncMock()
        mock_cmdio.message.content = '1d20'
        command = commands.RollCommand()
        asyncio.get_event_loop().run_until_complete(command.run(mock_cmdio))

        mock_send = mock_cmdio.message.channel.send
        mock_send.assert_called_once()
        self.assertEqual(mock_send.call_args[0][0], '**20**\n(20)')


if __name__ == '__main__':
    unittest.main()
