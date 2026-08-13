function toggleDevice(deviceId) {

    fetch(`/toggle/${deviceId}`, {
        method: "POST"
    })

    .then(response => response.json())

    .then(data => {

        if (data.success) {

            const statusElement =
                document.getElementById(
                    `status-${deviceId}`
                );

            statusElement.textContent =
                data.status;


            if (data.status === "ON") {

                statusElement.classList.remove("off");

                statusElement.classList.add("on");

            } else {

                statusElement.classList.remove("on");

                statusElement.classList.add("off");

            }


            location.reload();

        } else {

            alert(data.message);

        }

    })

    .catch(error => {

        console.error(error);

        alert(
            "Unable to communicate with the server."
        );

    });
}