# NPM Library

> Source: https://help.qsys.com/Content/External_Control_APIs/QRWC/qrwc_npm_library.htm

# NPM Library

Q-SYS Remote WebSocket Control (QRWC) is an Node Package (NPM) library designed to facilitate the interaction between third-party software and Q-SYS design controls. It enables developers to manage and control Q-SYS components through WebSocket connections, providing a seamless integration experience. For more detailed information, visit the [NPM Library](https://www.npmjs.com/package/@q-sys/qrwc).

**Note:** This is a BETA feature. Though it is functional, it is not feature complete and is subject to change. QSC assumes no responsibility for any issues that may arise from using this feature.

[Repository Purpose](javascript:void(0))

The QRWC repository is intended for developers who need to integrate their software with Q-SYS systems. It requires Q-SYS Designer Software version 10.0 or higher. The library offers robust tools for controlling and monitoring Q-SYS components, making it easier to develop custom control applications.

[Requirements](javascript:void(0))

1. QDS Version 10.0 or newer
2. NodeJS
3. QRWC NPM package

[Getting Started](javascript:void(0))

To begin using QRWC, developers need to import the library and establish a WebSocket connection to the Q-SYS Core. The library provides methods for attaching WebSocket connections, starting the control process, and accessing updated components and controls. This setup allows for real-time communication and control adjustments, ensuring efficient and responsive integration.

To install QRWC using NPM, use the following PowerShell command in your JavaScript app directory:

`npm install @q-sys/qrwc`

[Optional QRWC Parameters](javascript:void(0))

| Properties | | | |
| --- | --- | --- | --- |
| Name | NPM Library Naming | Attribute | Comment |
| Polling Interval | pollingInterval | number | Interval in milliseconds for polling control changes. The default polling rate is 350, or roughly 3 times a second |
| Component Filter | componentFilter | (componentState: IComponentState) => boolean | Filter function callback to allow for connecting to only specific components in a design. The default is to discover all script access âExternalâ or âAllâ components in the design. |
| Timeout Interval | timeout | number | Timeout interval in milliseconds for WebSocket messages. Default timeout is 5000. |
| If no options are provided for the following parameters, QRWC will initialize the socket to the default settings. | | | |

[Documentation](javascript:void(0))

For the full documentation, please visit the [Q-SYS NPM Package](https://www.npmjs.com/package/@q-sys/qrwc).
