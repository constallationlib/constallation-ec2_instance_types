from instance_type import InstanceType

x1e_xlarge = InstanceType(
    instance_family="x1e",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=4,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=122.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

x1e_2xlarge = InstanceType(
    instance_family="x1e",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=8,
    architecture="x86_64",
    cores=8,
    valid_cores=[2, 4, 8],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=244.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

x1e_4xlarge = InstanceType(
    instance_family="x1e",
    instance_size="4xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=16,
    architecture="x86_64",
    cores=16,
    valid_cores=[4, 8, 16],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=488.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

x1e_8xlarge = InstanceType(
    instance_family="x1e",
    instance_size="8xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=32,
    architecture="x86_64",
    cores=32,
    valid_cores=[8, 16, 32],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=976.0,
    storage_gb=None,
    storage_type=None,
    network_performance="10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

x1e_16xlarge = InstanceType(
    instance_family="x1e",
    instance_size="16xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=64,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=1952.0,
    storage_gb=None,
    storage_type=None,
    network_performance="20 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

x1e_32xlarge = InstanceType(
    instance_family="x1e",
    instance_size="32xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=128,
    architecture="x86_64",
    cores=128,
    valid_cores=[32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.3,
    memory_gb=3904.0,
    storage_gb=None,
    storage_type=None,
    network_performance="25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)