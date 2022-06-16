from pysgi import PySGI
from pysgi import Response

from esp32_connection import get_temp

app = PySGI()


@app.route('/api/temp')
def temp():
    data = get_temp()

    json_data = {
        'temperature': data[0],
        'humidity': data[1]
    }

    return Response(json_data, content_type='application/json')


app.run(host='0.0.0.0', port=5500)
