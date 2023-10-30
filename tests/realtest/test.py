import aiohttp
import asyncio
import pymelcloud


async def main():

    async with aiohttp.ClientSession() as session:
        # call the login method with the session
        token = await pymelcloud.login("email", "password", session=session)

        # lookup the device
        devices = await pymelcloud.get_devices(token, session=session)
        device = devices[pymelcloud.DEVICE_TYPE_ATW][0]

        # perform logic on the device
        await device.update()

        print(device.name)
        print(device.zones[0].flow_temperature)
        print(device.zones[0].return_temperature)
        print(device.zones[0].target_hc_temperature)
        print(device.zones[1].flow_temperature)
        print(device.zones[1].return_temperature)
        print(device.zones[1].target_hc_temperature)
        print(device.heat_pump_frequency)
        await session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
