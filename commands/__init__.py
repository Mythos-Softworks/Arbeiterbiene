from commands.aqi_command import AqiCommand
from commands.base_command import BaseCommand
from commands.command_io import CommandIO
from commands.die_command import DieCommand
from commands.meow_command import MeowCommand
from commands.poll_command import PollCommand
from commands.repost_command import RepostCommand
from commands.roll_command import RollCommand
from commands.scion_command import ScionCommand
from commands.woof_command import WoofCommand


def command_registry():
    return {
        AqiCommand.trigger_word(): AqiCommand(),
        DieCommand.trigger_word(): DieCommand(),
        MeowCommand.trigger_word(): MeowCommand(),
        PollCommand.trigger_word(): PollCommand(),
        RepostCommand.trigger_word(): RepostCommand(),
        RollCommand.trigger_word(): RollCommand(),
        ScionCommand.trigger_word(): ScionCommand(),
        WoofCommand.trigger_word(): WoofCommand()
    }
