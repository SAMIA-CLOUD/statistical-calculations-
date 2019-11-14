def fetchRawdata(data, str):
    d = []
    for row in data.data:
        d.append(row[str])
    return d
