import subprocess

class installers :
    def  run_installer_nginx():
        try:
            result = subprocess.run(
                ["bash", "scripts/install_nginx.sh"],
                check=True,
                capture_output=True,
                text=True
            )
            print("script output:")
            print(result.stdout)
            #logging.info("install nginx correctly")
        except subprocess.CalledProcessError as err:
            print("script failed with error:")
            #logging.error(f"failed to install nginx do yo {err}")
            print(err.stderr)

        except FileNotFoundError:
            print("cant not found bash script ")

    def  run_installer_pydantic():
        try:
            result = subprocess.run(
                ["bash","scripts/install_pydantic.sh"],
                check=True,
                capture_output=True,
                text=True
            )
            print("script output:")
            #logging.info("install pydantic correctly")
            print(result.stdout)

        except subprocess.CalledProcessError as err:
            print("script failed with error:")
            #logging.error(f"failed to install pydantic do yo {err}")
            print(err.stderr)

        except FileNotFoundError:
            print("cant not found bash script ")     


