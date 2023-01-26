import asyncio
import click
from functions import *


@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
@click.option('--reload', '-r', 'reload', is_flag=True,
              help='enables hot reloading. (When changes are made to" SOURCE " file, shrtcutCSS automatically generates the CSS.)')
@click.option('--genmode', help='choose how you want the random class names to be generated', required=False, type=click.Choice(["123", "xyz"]), default="123")
def shrtcutcli(source, output, reload, genmode):
    '''
    shrtcutCSS is designed to make styling your webpages faster and more efficient  \n
    shrtcutCSS watches the " SOURCE " file
    and generates css codes based on the "scc" attribute you add to different HTML elements.
    Then it will save the codes to the " OUTPUT " file.
    (If the file does not exist , It will be created for you). \n
    To learn more please visit : \n
    '''
    if not reload:
        css_dict = css_parser(output)
        new_cass = dict_to_css(scc_interpreter(source, css_dict))
        with open(output,"w") as file:
            file.write(new_cass)
    else:
        print("Hello world!")
