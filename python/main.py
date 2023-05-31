import sys

from build_metainfo import *
from resolve_download import *

if __name__ == "__main__":
    is_studio = '--studio' in sys.argv
    app_tag = "davinci-resolve-studio" if is_studio else "davinci-resolve"

    print("Building for tag " + app_tag)

    print("Requesting version information...")
    (version, release_id, download_id) = get_latest_version_information(
        refer_id='77ef91f67a9e411bbbe299e595b4cfcc',
        app_tag=app_tag,
    )
    print(f"Download latest version of Davinchi Resolve{' Studio' if is_studio else ''}...")
    download_using_id(download_id)
    print(f"Building meta info...")
    build_metainfo(
        app_id='com.blackmagic.ResolveStudio' if is_studio else 'com.blackmagic.Resolve',
        app_description="DaVinci Resolve Studio" if is_studio else 'DaVinchi Resolve',
        app_tag=app_tag,
    )
