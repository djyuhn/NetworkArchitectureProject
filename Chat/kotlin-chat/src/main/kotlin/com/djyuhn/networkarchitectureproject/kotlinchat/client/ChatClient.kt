package com.djyuhn.networkarchitectureproject.kotlinchat.client

import java.io.*
import java.net.Socket
import java.nio.ByteBuffer
import java.nio.charset.Charset

/**
 * @author djyuhn
 * 3/27/2019
 */
class ChatClient(private val ip: String, private val port: Int) {

    private val socket: Socket = Socket(ip, port)
    private val send: BufferedOutputStream
    private val receive: BufferedInputStream

    init {
        send = BufferedOutputStream(socket.getOutputStream())
        receive = BufferedInputStream(socket.getInputStream())
    }

    fun sendMessage(message: String) {
        val messageLength = ByteBuffer.allocate(4) // Send message length integer as fixed size
        messageLength.putInt(message.length)
        send.write(messageLength.array())
        send.write(message.toByteArray())
        send.flush()
    }

    fun receiveMessage(): String {
        val messageLength = ByteArray(4)
        receive.read(messageLength, 0, messageLength.size)
        val message = ByteArray(ByteBuffer.wrap(messageLength).int)
        receive.read(message, 0, message.size)
        return String(message)
    }

    fun stopConnection() {
        receive.close()
        send.close()
        socket.close()
    }
}