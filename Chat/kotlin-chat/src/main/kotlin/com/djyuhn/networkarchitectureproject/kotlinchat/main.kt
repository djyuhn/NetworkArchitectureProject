package com.djyuhn.networkarchitectureproject.kotlinchat

import com.djyuhn.networkarchitectureproject.kotlinchat.client.ChatClient

/**
 * @author djyuhn
 * 3/27/2019
 */

fun main(args: Array<String>) {
    val ip = "10.10.1.1"
    val port = 5000

    val chatClient = ChatClient(ip, port)

    println("Enter your message: ")
    var userInput = readLine()!!

    while (userInput.toLowerCase() != "exit") {
        val data = chatClient.sendMessage(userInput)
        println("Server Response:: $data")
        println("Enter your message: ")
        userInput = readLine()!!
    }

    val data = chatClient.sendMessage(userInput)
    println("Server Response:: $data")
    chatClient.stopConnection()

}