def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    backRow = blueShirtHeights
    frontRow = redShirtHeights

    if redShirtHeights[0] > blueShirtHeights[0]:
        backRow = redShirtHeights
        frontRow = blueShirtHeights

    for idx in range(len(backRow)):
        if backRow[idx] <= frontRow[idx]:
            return False
    return True