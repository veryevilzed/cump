#!/usr/bin/env python
#coding:utf-8

import check
import click, setup

@click.group()
@click.pass_context
@click.option('--settings', '-s', default="~/.cump/cump.cfg", type=click.Path(exists=False, file_okay=True, readable=True, dir_okay=False), help='credentials.ini file path')
@click.option('--s3-access-key',  help='S3 access key')
@click.option('--s3-public-key',  help='S3 public key')
@click.option('--s3-bucket',  help='S3 bucket')
@click.option('--http-auth',  help='Http Basic-Authentication')
@click.option('--http-host',  help='Host of repository')
@click.option('--project', '-p', type=click.Path(exists=True, file_okay=True, readable=True, dir_okay=False), help='Project file path')
@click.option('--verbose', '-v', default=False, type=bool, is_flag=True, help='Verbose')
def cli(ctx, settings, s3_access_key, s3_public_key, s3_bucket, http_auth, http_host, project, verbose):
    ctx.obj['settings_path'] = settings
    ctx.obj['s3_access_key'] = s3_access_key
    ctx.obj['s3_public_key'] = s3_public_key
    ctx.obj['s3_bucket'] = s3_bucket
    ctx.obj['http_auth'] = http_auth
    ctx.obj['http_host'] = http_host
    ctx.obj['project'] = project
    ctx.obj['verbose'] = verbose


@cli.command()
def dropdb():
    click.echo('Dropped the database')


cli.add_command(check.check)
cli.add_command(setup.setup)
cli.add_command(dropdb)


if __name__ == '__main__':
    cli(obj={})