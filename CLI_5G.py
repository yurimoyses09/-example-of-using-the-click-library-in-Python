# -*- coding: utf-8 -*-

"""
Click is a Python package for creating beautiful command line interfaces in a composable way with as 
little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but 
comes with sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun while also preventing any 
frustration caused by the inability to implement an intended CLI API.

Click in three points:

-> Arbitrary nesting of commands;

-> Automatic help page generation;

-> Supports lazy loading of subcommands at runtime
"""

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
    if bsstart != 'bsstart' or bsstart == '':
        click.echo('{} - Command Invalid!'.format(bsstart))
    else:
        click.echo('OK')
    click.pause(info='Press any key to continue...')


@main.command('uestart', short_help='MAC/PHY Initialization and Static configuration parameter load related to UE;')
def uestart():
    if uestart != 'uestart' or uestart == '':
        click.echo('{} - Command Invalid!'.format(uestart))
    else:
        click.echo('OK')
    click.pause(info='Press any key to continue...')  # info -> This command stops execution and waits for the user
    # to press any key to continue.


@main.command('stopprocess', short_help='MAC/PHY termination;')
def stopprocess():
    if stopprocess != 'stopprocess' or stopprocess == '':
        click.echo('{} - Command Invalid!'.format(stopprocess))
    else:
        click.echo('MAC and PHY were successfully stopped')
    click.pause(info='Press any key to continue...')


# short_help -> put a short help to the command
@main.command('sets', short_help='Dynamic parameters configuration, issued only on the BS side;')
@click.argument('argument', type=str)  # argument -> ulreservation
# type=click.IntRange() delimitation or input value
# nargs -> delimits the amount of values entered
@click.argument('ueid', type=click.IntRange(0, 15))
@click.argument('rbstart', type=click.IntRange(0, 132), nargs=1)
@click.argument('numrb', type=click.IntRange(0, 132), nargs=1)
def sets(argument):
    if argument != 'ulreservation' or argument == '':
        click.echo('{} - Argument Invalid'.format(argument))  # if the argument entered is wrong or None
    elif sets != 'sets' or sets == '':
        click.echo('{} - Command Invalid'.format(sets))  # If the command entered is wrong ou None 
    else:  # if the values and data are correct
        click.echo('The values entered are correct')
    click.pause(info='\nPress any key to continue...')


@main.command('get', short_help='Show values: UEID, RBStart, NumRB;')  # Attaches an argument to the command
@click.argument('argument')
def get(argument):
    if argument != 'ulreservation' or argument == '':  
        click.echo('{} - Argument Invalid'.format(argument))  # if the argument entered is wrong or None
    else:
        ueid = randint(1, 1)
        rbstart = randint(1, 132)
        numrb = randint(1, 132)
        click.echo('UlReservation: <{}> <{}> <{}>'.format(ueid, rbstart, numrb))
    click.pause(info='\nPress any key to continue...')


if __name__ == '__main__':
    main(prog_name='CLI 5G')
