# -*- coding: utf-8 -*-

"""Click is a simple Python module inspired by the stdlib optparse to make
writing command line scripts fun."""
import click
from random import randint

# dict() -> new empty dictionary
CONTEXT_SETTINGS = dict(help_option_names=['--help', '-h'])  # help options


# invoke_without_command=True -> forces the application not to show aids before losing them with a --h
@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
def main():
    pass


@main.command('bsstart', short_help='MAC/PHY Initialization and Static configuration parameter load related to BS;')
def bsstart():
    # click.echo()-> Prints a message plus a newline to the given file or stdout
    click.echo('OK')
    click.pause(info='Press any key to continue...')


@main.command('uestart', short_help='MAC/PHY Initialization and Static configuration parameter load related to UE;')
def uestart():
    click.echo('OK')
    click.pause(info='Press any key to continue...')  # info -> This command stops execution and waits for the user
    # to press any key to continue.


@main.command('stopprocess', short_help='MAC/PHY termination;')
def stopprocess():
    click.echo('MAC and PHY were successfully stopped')
    click.pause(info='Press any key to continue...')


# short_help -> put a short help to the command
# @main.command('sets', short_help='Dynamic parameters configuration, issued only on the BS side;')
@click.argument('argument', type=str)
# type=click.IntRange() delimitation or input value
# nargs -> delimits the amount of values entered
@click.argument('ueid', type=click.IntRange(0, 15))
@click.argument('rbstart', type=click.IntRange(0, 132), nargs=1)
@click.argument('numrb', type=click.IntRange(0, 132), nargs=1)
def sets(argument):
    if argument != 'ulreservation':
        click.echo('{} - Argument Invalid'.format(argument))  # if the argument entered is wrong
    else:
        click.echo('The values entered are correct')
    click.pause(info='\nPress any key to continue...')


@main.command('get', short_help='Show values: UEID, RBStart, NumRB;')  # Attaches an argument to the command
@click.argument('argument')
def get(argument):
    if argument != 'ulreservation':
        click.echo('{} - Argument Invalid'.format(argument))  # if the argument entered is wrong
    else:
        ueid = randint(1, 1)
        rbstart = randint(1, 132)
        numrb = randint(1, 132)
        click.echo('UlReservation: <{}> <{}> <{}>'.format(ueid, rbstart, numrb))
    click.pause(info='\nPress any key to continue...')


if __name__ == '__main__':
    main(prog_name='CLI 5G')
