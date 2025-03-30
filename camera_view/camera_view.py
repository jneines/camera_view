"""
A simple qt based camera display app.

Shows streams of supported cameras in a window.
Also works for framegrabber devices that the os supports.
"""
import sys

from qtpy.QtCore import Qt
from qtpy.QtGui import QKeyEvent
from qtpy.QtWidgets import QApplication
from qtpy.QtMultimedia import QCamera, QCameraInfo
from qtpy.QtMultimediaWidgets import QCameraViewfinder

from loguru import logger
import click


class CameraView(QCameraViewfinder):
    def __init__(self, parent=None):
        QCameraViewfinder.__init__(self)
        self.available_cameras = QCameraInfo.availableCameras()
        self.show_fullscreen = False

    def select_camera(self, i):
        """Allow selecting the 'camera' to be used."""
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self)
        self.camera.start()

    def keyPressEvent(self, event):
        """Process key_press events."""

        if event.key() == Qt.Key_F:
            self.show_fullscreen = not self.show_fullscreen
            if self.show_fullscreen:
                logger.info("Going fullscreen")
                self.showFullScreen()
            else:
                logger.info("Returning to normal")
                self.showNormal()

        elif event.key() == Qt.Key_Q:
            logger.info("Exiting app")
            QApplication.quit()


def configure_logging(ctx, param, verbose):
    """Configure logging using command line parameters."""
    level_list = ["WARNING", "INFO", "DEBUG"]
    _log_level = level_list[verbose]
    logger.remove()
    logger.add(sys.stdout, level=_log_level)


@click.command()
@click.option(
    "-v",
    "--verbose",
    count=True,
    callback=configure_logging,
    expose_value=False,
    default=0,
)
@click.option(
    "-d",
    "--device-id",
    type=int,
    required=True,
    default=0,
    show_default=True,
    help="Device id to use",
)
@click.option("-f", "--fullscreen", is_flag=True, help="Start in fullscreen mode")
def main(device_id, fullscreen):

    app = QApplication(sys.argv)

    camera_view = CameraView()
    camera_view.select_camera(device_id)

    if fullscreen:
        # fullscreen display requested.
        # send appropriate key event to make the app switch to fullscreen
        event = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_F, Qt.KeyboardModifier.NoModifier)
        app.sendEvent(camera_view, event)

    camera_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
