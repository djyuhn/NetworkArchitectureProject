package com.djyuhn.networkarchitectureproject.kotlinchat

import com.djyuhn.networkarchitectureproject.kotlinchat.client.ChatClient
import kotlin.concurrent.thread
import java.net.InetAddress


/**
 * @author djyuhn
 * 3/27/2019
 */

fun main() {
    val ip = "204.76.187.50"
    val port = 5000

    val chatClient = ChatClient(ip, port)
    val clientAddress = InetAddress.getLocalHost()

    println(chatClient.receiveMessage())

    thread(start = true) {
        var received = chatClient.receiveMessage()
        while (received != "${clientAddress.hostAddress}#quit") {
            println(received)
            received = chatClient.receiveMessage()
        }
        println(received)
    }

    var userInput = readLine()!!
    while (userInput.toLowerCase() != "#quit") {
        chatClient.sendMessage(userInput)
        userInput = readLine()!!
    }

    chatClient.sendMessage(userInput)
    Thread.sleep(200)
    chatClient.stopConnection()
}