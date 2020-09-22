import datetime


def doScreen(obj, folder, nameFile, screenType):
    screenshotName = folder + screenType + "_" + nameFile + "_" + str(datetime.date.today()) + ".png"
    obj.get_screenshot_as_file(screenshotName)
