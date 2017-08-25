import ConfigParser

import click, os
import errno


@click.command(name="setup")
@click.pass_context
def setup(ctx):
    """Setup your cump
    """
    click.echo("Setup repository")
    host = click.prompt('Please enter a repository host', type=str, default="http://localhost:8989/repo/")
    user = click.prompt('Please enter a repository user', type=str)
    passwd = click.prompt('Please enter a repository password', type=str)


    if click.confirm('save %s?' % ctx.obj["settings_path"]):
        click.echo("saving...")
        config = ConfigParser.ConfigParser()
        path = ctx.obj["settings_path"]
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
                click.echo("saving...")
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        else:
            config.read(path)

        if not config.has_section("repository"):
            config.add_section("repository")
        config.set("repository", "host", host)
        config.set("repository", "user", user)
        config.set("repository", "passwd", passwd)
        with open(path, 'wb') as configfile:
            config.write(configfile)
