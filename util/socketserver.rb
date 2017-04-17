require 'socket'


port = ARGV.shift
server = TCPServer.new port

puts "Listening on tcp/#{port}"
loop do
  Thread.start(server.accept) do |client|
    puts "Got a connection from #{client.peeraddr[3]}"
  end
end
