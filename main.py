import requests
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)

@app.route("/parking-management")
def index():
    return redirect(url_for('dashboard'))

# ------------------ DASHBOARD ---------------------
@app.route("/parking-management/dashboard")
def dashboard():
    totalCars = requests.get("http://localhost:8080/dashboard/total-cars").json()
    totalActiveParkings = requests.get("http://localhost:8080/dashboard/total-active-parkings").json()
    totalLots = requests.get("http://localhost:8080/dashboard/total-parking-lots").json()
    totalUnoccupiedLots = requests.get("http://localhost:8080/dashboard/total-unoccupied-parking-lots").json()
    totalPaidPaymentsToday = requests.get("http://localhost:8080/dashboard/total-paid-payments-value-today").json()
    totalPendingPayments = requests.get("http://localhost:8080/dashboard/total-pending-payments").json()
    return render_template("dashboard.html", totalCars=totalCars, totalActiveParkings=totalActiveParkings,
                           totalLots=totalLots, totalUnoccupiedLots=totalUnoccupiedLots,
                           totalPaidPaymentsToday=totalPaidPaymentsToday, totalPendingPayments=totalPendingPayments)

# ------------------ PARKING LOTS ---------------------
@app.route("/parking-management/parking-lots/filter/<int:filter>", methods=["GET", "POST"])
def parkingLots(filter):
    match filter:
        case 1:
            req = requests.get("http://localhost:8080/parkingLots").json()
        case 2:
            req = requests.get("http://localhost:8080/parkingLots/unoccupied").json()
        case 3:
            req = requests.get("http://localhost:8080/parkingLots/occupied").json()
    return render_template("parkingLots.html", parkingLots=req)

@app.route("/parking-management/parking-lots/create", methods=["GET", "POST"])
def createParkingLot():
    if request.method == "GET":
        return render_template("createParkingLot.html")
    if request.method == "POST":
        tag = request.form.get("tag")
        data = {"tag": tag}
        req = requests.post("http://localhost:8080/parkingLots", json=data)
        return redirect(url_for("parkingLots", filter=1))
    
@app.route("/parking-management/parking-lots/delete/<int:id>", methods=["GET", "POST"])
def deleteParkingLot(id):
    req = requests.delete(f"http://localhost:8080/parkingLots/{id}")
    return redirect(url_for("parkingLots", filter=1))

@app.route("/parking-management/parking-lots/edit/<int:id>", methods=["GET", "POST"])
def editParkingLot(id):
    if request.method == "GET":
        parkingLot = requests.get(f"http://localhost:8080/parkingLots/{id}").json()
        return render_template("editParkingLot.html", parkingLot=parkingLot)
    if request.method == "POST":
        data = {"tag": request.form.get("tag")}
        req = requests.put(f"http://localhost:8080/parkingLots/{id}", json=data)
        return redirect(url_for("parkingLots", filter=1))

# ------------------ CARS ---------------------
@app.route("/parking-management/cars")
def cars():
    req = requests.get("http://localhost:8080/cars").json()
    return render_template("cars.html", cars=req)

@app.route("/parking-management/cars/create", methods=["GET", "POST"])
def createCar():
    if request.method == "GET":
        return render_template("createCar.html")
    if request.method == "POST":
        data = {"licensePlate": request.form.get("licensePlate"), "brand": request.form.get("brand"), "model": request.form.get("model"), "color": request.form.get("color")}
        req = requests.post("http://localhost:8080/cars", json=data)
        return redirect(url_for("cars"))
    
@app.route("/parking-management/cars/delete/<int:id>", methods=["GET", "POST"])
def deleteCar(id):
    req = requests.delete(f"http://localhost:8080/cars/{id}")
    return redirect(url_for("cars"))

@app.route("/parking-management/cars/edit/<int:id>", methods=["GET", "POST"])
def editCar(id):
    if request.method == "GET":
        car = requests.get(f"http://localhost:8080/cars/{id}").json()
        return render_template("editCar.html", car=car)
    if request.method == "POST":
        data = {"licensePlate": request.form.get("licensePlate"), "brand": request.form.get("brand"), "model": request.form.get("model"), "color": request.form.get("color")}
        req = requests.put(f"http://localhost:8080/cars/{id}", json=data)
        return redirect(url_for("cars"))
    
@app.route("/parking-management/cars/parkings/<int:id>/filter/<int:filter>", methods=["GET"])
def carParkings(id, filter):
    if request.method == "GET":
        match filter:
            case 1:
                parkings = requests.get(f"http://localhost:8080/parkings/search?carId={id}").json()
            case 2:
                parkings = requests.get(f"http://localhost:8080/parkings/going?carId={id}").json()
            case 3:
                parkings = requests.get(f"http://localhost:8080/parkings/ended?carId={id}").json()
        car = requests.get(f"http://localhost:8080/cars/{id}").json()
        return render_template("carParkings.html", parkings=parkings, car=car)

# ------------------ PARKINGS ---------------------
@app.route("/parking-management/parkings/filter/<int:filter>")
def parkings(filter):
    match filter:
        case 1:
            req = requests.get("http://localhost:8080/parkings").json()
        case 2:
            req = requests.get("http://localhost:8080/parkings/going").json()
        case 3:
            req = requests.get("http://localhost:8080/parkings/ended").json()
    return render_template("parkings.html", parkings=req)

@app.route("/parking-management/parkings/create", methods=["GET", "POST"])
def createParking():
    if request.method == "GET":
        cars = requests.get("http://localhost:8080/cars/inParkingFalse").json()
        parkingLots = requests.get("http://localhost:8080/parkingLots/unoccupied").json()
        return render_template("createParking.html", cars=cars, parkingLots=parkingLots)
    if request.method == "POST":
        url = "http://localhost:8080/parkings/insert?carId={carId}&parkingLotId={parkingLotId}"
        data = {"startTime": request.form.get("startTime"), "rate": request.form.get("rate")}
        carId = request.form["carId"]
        parkingLotId = request.form["parkingLotId"]
        url = url.format(carId=carId, parkingLotId=parkingLotId)
        req = requests.post(url, json=data)
        return redirect(url_for("parkings", filter=1))
    
@app.route("/parking-management/parkings/delete/<int:id>", methods=["GET", "POST"])
def deleteParking(id):
    req = requests.delete(f"http://localhost:8080/parkings/{id}")
    return redirect(url_for("parkings", filter=1))
    
@app.route("/parking-management/parkings/end/<int:id>")
def endParking(id):
    time = datetime.now().strftime('%H:%M')
    req = requests.get(f"http://localhost:8080/parkings/end/{id}?endTime={time}")
    return redirect(url_for("parkings", filter=1))

@app.route("/parking-management/parkings/generate-payment/<int:id>")
def generatePayment(id):
    data = {}
    req = requests.post(f"http://localhost:8080/payments/insert?parkingId={id}", json=data)
    return redirect(url_for("payments", filter=1))
    
# ------------------ PAYMENTS ---------------------
@app.route("/parking-management/payments/filter/<int:filter>")
def payments(filter):
    match filter:
        case 1:
            req = requests.get("http://localhost:8080/payments").json()
        case 2:
            req = requests.get("http://localhost:8080/payments/paid").json()
        case 3:
            req = requests.get("http://localhost:8080/payments/pending").json()        
    return render_template("payments.html", payments=req)

@app.route("/parking-management/payments/end/<int:id>")
def endPayment(id):
    req = requests.get(f"http://localhost:8080/payments/end/{id}")
    return redirect(url_for("payments", filter=1))

@app.route("/parking-management/payments/delete/<int:id>")
def deletePayment(id):
    req = requests.delete(f"http://localhost:8080/payments/{id}")
    return redirect(url_for("payments", filter=1))

if __name__ == "__main__":
    app.run(debug=True)