from tethys_sdk.app_settings import CustomSetting, SpatialDatasetServiceSetting
from tethys_sdk.base import TethysAppBase, url_map_maker


class nasaaccess(TethysAppBase):
    """
    Tethys app class for nasaaccess.
    """

    name = "NASAaccess"
    index = "home"
    icon = "nasaaccess/images/nasaaccess.png"
    package = "nasaaccess"
    root_url = "nasaaccess"
    color = "#3e557a"
    description = "Web interface for accessing and visualizing climate and weather data from NASA's Earth Observing System Data and Information System (EOSDIS)"
    tags = "NASA, Hydrology, Climate, Weather, GPM, TRMM, GLDAS, CMIP5, CMIP6"
    enable_feedback = False
    feedback_emails = []
    controller_modules = [ "controllers", "ajax_controllers"]

    # custom settings ##
    def custom_settings(self):
        """
        Example custom_settings method.
        """
        custom_settings = (
            CustomSetting(
                name="data_path",
                type=CustomSetting.TYPE_STRING,
                description="Data Directory for Downloads",
                required=False,
            ),
            CustomSetting(
                name="nasaaccess_R",
                type=CustomSetting.TYPE_STRING,
                description="R interpreter",
                required=False,
            ),
            CustomSetting(
                name="nasaaccess_script",
                type=CustomSetting.TYPE_STRING,
                description="Path to the nasaaccess R script file",
                required=False,
            ),
            CustomSetting(
                name="geoserver_workspace",
                type=CustomSetting.TYPE_STRING,
                description="Geoserver Workspace",
                required=False,
            ),
            CustomSetting(
                name="geoserver_URI",
                type=CustomSetting.TYPE_STRING,
                description="Geoserver URI",
                required=False,
            ),
            CustomSetting(
                name="geoserver_user",
                type=CustomSetting.TYPE_STRING,
                description="Geoserver User",
                required=False,
            ),
            CustomSetting(
                name="geoserver_password",
                type=CustomSetting.TYPE_STRING,
                description="Geoserver Password",
                required=False,
            ),
        )

        return custom_settings

    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name="ADPC",
                description="GeoServer service for the shapefiles and DEMS files.",
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings
