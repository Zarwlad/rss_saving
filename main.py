import rss.lenta_rss_client as rss
import config.log
import cmd_xsd

# cmd_xsd.ex()
config.log.conf()
rss.get_lenta_dto(rss.get_rss())

