from configparser import ConfigParser

from src.constants.path_constants import IMG_GENERATION_CFG_PATH


class PlotConfig:

    PLOT_CONFIG = ConfigParser()
    PLOT_CONFIG.read(IMG_GENERATION_CFG_PATH)