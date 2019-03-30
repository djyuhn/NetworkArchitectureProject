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

    println(chatClient.receiveMessage())

    var userInput = readLine()!!

    while (userInput.toLowerCase() != "#quit") {
        val data = chatClient.sendMessage(userInput)
        println("Server-> $data")
        print("Enter your message: ")
        userInput = readLine()!!
    }

    val data = chatClient.sendMessage(userInput)
    println("Server responded with: $data")
    chatClient.stopConnection()

}